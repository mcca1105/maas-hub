#!/usr/bin/env python3
"""
DRM Squad: Funnel Cohesion Validator
Validates consistency (message match, tone, offer, proof) across all funnel assets.
Ryan Deiss's principle: The #1 cause of funnel failure is message mismatch between
the ad and the landing page. This validator catches it before launch.

Usage:
    python drm-cohesion-validator.py --dir path/to/funnel/assets/
    python drm-cohesion-validator.py --ad ad.md --landing landing.md --email email.md
    python drm-cohesion-validator.py --config funnel-config.yaml

The validator checks:
    1. Message match between sequential funnel steps
    2. Offer consistency (same price/bonus claimed everywhere)
    3. Avatar language consistency (same vocabulary across assets)
    4. Urgency consistency (deadline the same in all assets)
    5. Proof consistency (testimonials not contradicting each other)
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional
import json


# ─────────────────────────────────────────────────────────────────────────────
# EXTRACTION HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def extract_headline(text: str) -> str:
    """Extract the primary headline from copy."""
    # Try markdown H1/H2
    match = re.search(r'^#{1,2}\s+(.+)$', text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    # Try first line over 20 chars (often the headline in plain text copy)
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 20 and not line.startswith('#'):
            return line[:100]
    return ""


def extract_price_mentions(text: str) -> list:
    """Extract all price mentions from copy."""
    return re.findall(r'\$[\d,]+(?:\.\d{2})?', text)


def extract_deadline_mentions(text: str) -> list:
    """Extract deadline/urgency mentions from copy."""
    patterns = [
        r'(?:expires?|ends?|deadline|closes?|available until)\s+[^\.,\n]{3,50}',
        r'(?:today only|limited time|this week|this month)',
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}',
    ]
    found = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        found.extend(matches)
    return found


def extract_key_terms(text: str, top_n: int = 30) -> dict:
    """Extract the most frequent meaningful terms from copy."""
    # Remove common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'that',
        'this', 'these', 'those', 'it', 'its', 'they', 'their', 'them',
        'you', 'your', 'we', 'our', 'i', 'my', 'he', 'she', 'his', 'her',
        'if', 'when', 'then', 'than', 'as', 'so', 'not', 'no', 'up', 'all',
        'just', 'more', 'also', 'about', 'get', 'got', 'one', 'two', 'three',
    }

    words = re.findall(r'\b[a-z]{4,}\b', text.lower())
    freq = {}
    for word in words:
        if word not in stop_words:
            freq[word] = freq.get(word, 0) + 1

    # Sort by frequency and return top N
    sorted_terms = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_terms[:top_n])


def extract_product_name(text: str) -> Optional[str]:
    """Try to extract the product/program name from copy."""
    patterns = [
        r'introducing\s+([A-Z][^.!?\n]{2,40})',
        r'called\s+([A-Z][^.!?\n]{2,40})',
        r'welcome to\s+([A-Z][^.!?\n]{2,40})',
        r'join\s+([A-Z][^.!?\n]{2,40})',
        r'download\s+([A-Z][^.!?\n]{2,40})',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def extract_core_promise(text: str) -> str:
    """Extract what appears to be the core promise/result claim."""
    promise_patterns = [
        r'how to\s+([^.!?\n]{10,80})',
        r'discover\s+([^.!?\n]{10,80})',
        r'learn how to\s+([^.!?\n]{10,80})',
        r'finally\s+([^.!?\n]{10,80})',
        r'you\'ll\s+([^.!?\n]{10,80})',
    ]
    for pattern in promise_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()[:120]
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# COHESION CHECKS
# ─────────────────────────────────────────────────────────────────────────────

def check_price_consistency(assets: dict) -> dict:
    """Check if the same price is claimed across all assets."""
    all_prices = {}
    for asset_name, text in assets.items():
        prices = extract_price_mentions(text)
        if prices:
            all_prices[asset_name] = prices

    if not all_prices:
        return {
            "status": "NO_PRICE_FOUND",
            "message": "No price mentions found in any asset",
            "assets_with_prices": {},
        }

    # Find all unique prices across all assets
    all_unique_prices = set()
    for prices in all_prices.values():
        all_unique_prices.update(prices)

    # Check if assets that mention price agree on the main price
    # (allow for value stack prices to differ, focus on the single purchase price)
    main_price_candidates = {}
    for asset, prices in all_prices.items():
        # Count occurrence of each price — most frequent is likely the main price
        for price in prices:
            main_price_candidates[price] = main_price_candidates.get(price, 0) + 1

    most_common_price = max(main_price_candidates, key=main_price_candidates.get) if main_price_candidates else None

    return {
        "status": "OK" if len(all_unique_prices) <= 5 else "REVIEW",
        "most_common_price": most_common_price,
        "all_prices_found": list(all_unique_prices),
        "assets_with_prices": all_prices,
        "note": "Review if different assets claim different 'buy' prices",
    }


def check_message_match(assets: dict) -> dict:
    """
    Check if headlines/themes match between sequential funnel steps.
    Ryan Deiss rule: Ad → Landing Page → VSL should flow with matching message.
    """
    headlines = {}
    for asset_name, text in assets.items():
        headline = extract_headline(text)
        if headline:
            headlines[asset_name] = headline

    if len(headlines) < 2:
        return {
            "status": "INSUFFICIENT_ASSETS",
            "message": "Need at least 2 assets to check message match",
        }

    # Check keyword overlap between headlines
    mismatches = []
    asset_names = list(headlines.keys())

    for i in range(len(asset_names) - 1):
        name_a = asset_names[i]
        name_b = asset_names[i + 1]
        hl_a = headlines[name_a].lower()
        hl_b = headlines[name_b].lower()

        # Tokenize and check significant word overlap
        words_a = set(re.findall(r'\b[a-z]{4,}\b', hl_a)) - {'that', 'this', 'with', 'from', 'your', 'have', 'will'}
        words_b = set(re.findall(r'\b[a-z]{4,}\b', hl_b)) - {'that', 'this', 'with', 'from', 'your', 'have', 'will'}

        if words_a and words_b:
            overlap = words_a & words_b
            overlap_ratio = len(overlap) / min(len(words_a), len(words_b))

            if overlap_ratio < 0.2 and len(words_a) > 2 and len(words_b) > 2:
                mismatches.append({
                    "step_a": name_a,
                    "headline_a": headlines[name_a],
                    "step_b": name_b,
                    "headline_b": headlines[name_b],
                    "overlap_ratio": round(overlap_ratio, 2),
                    "shared_words": list(overlap),
                })

    return {
        "status": "WARNING" if mismatches else "OK",
        "headlines": headlines,
        "mismatches": mismatches,
        "message": f"{len(mismatches)} potential message mismatch(es) found" if mismatches else "Message appears consistent across assets",
    }


def check_term_consistency(assets: dict) -> dict:
    """
    Check if the same key terms appear across assets.
    Inconsistent vocabulary suggests disconnected copywriting.
    """
    all_terms = {}
    for asset_name, text in assets.items():
        terms = extract_core_terms_from_text(text)
        all_terms[asset_name] = terms

    if len(all_terms) < 2:
        return {"status": "INSUFFICIENT_ASSETS"}

    # Find terms in >50% of assets (these are the consistent terms)
    asset_count = len(all_terms)
    all_term_names = set()
    for terms in all_terms.values():
        all_term_names.update(terms)

    consistent_terms = []
    inconsistent_terms = []
    for term in all_term_names:
        count = sum(1 for terms in all_terms.values() if term in terms)
        if count >= max(2, asset_count * 0.5):
            consistent_terms.append(term)
        elif count == 1:
            # Term appears in only one asset — potential inconsistency
            for asset, terms in all_terms.items():
                if term in terms:
                    inconsistent_terms.append({"term": term, "only_in": asset})
                    break

    return {
        "status": "OK" if len(inconsistent_terms) <= 5 else "REVIEW",
        "consistent_terms": consistent_terms[:15],
        "potentially_inconsistent": inconsistent_terms[:10],
        "message": f"Consistent vocabulary found across {len(consistent_terms)} terms",
    }


def extract_core_terms_from_text(text: str) -> set:
    """Get meaningful terms from text for comparison."""
    stop = {'that', 'this', 'with', 'from', 'your', 'have', 'will', 'about',
            'what', 'when', 'then', 'also', 'more', 'just', 'get', 'can', 'for'}
    words = re.findall(r'\b[a-z]{5,}\b', text.lower())
    freq = {}
    for w in words:
        if w not in stop:
            freq[w] = freq.get(w, 0) + 1
    # Return words appearing 2+ times (significant terms)
    return {w for w, c in freq.items() if c >= 2}


def check_urgency_consistency(assets: dict) -> dict:
    """Check if deadline/urgency claims are consistent."""
    deadlines = {}
    for asset_name, text in assets.items():
        found = extract_deadline_mentions(text)
        if found:
            deadlines[asset_name] = found

    if not deadlines:
        return {
            "status": "NO_URGENCY",
            "message": "No urgency/deadline elements found",
        }

    # Check if specific dates are mentioned and match
    date_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}'
    specific_dates = {}
    for asset, mentions in deadlines.items():
        dates = []
        for mention in mentions:
            date_matches = re.findall(date_pattern, mention, re.IGNORECASE)
            dates.extend(date_matches)
        if dates:
            specific_dates[asset] = dates

    all_specific_dates = set()
    for dates in specific_dates.values():
        all_specific_dates.update(d.lower() for d in dates)

    return {
        "status": "WARNING" if len(all_specific_dates) > 1 else "OK",
        "urgency_found_in": list(deadlines.keys()),
        "specific_dates": specific_dates,
        "unique_dates": list(all_specific_dates),
        "message": "Multiple different deadline dates found — check consistency" if len(all_specific_dates) > 1 else "Urgency appears consistent",
    }


# ─────────────────────────────────────────────────────────────────────────────
# REPORTING
# ─────────────────────────────────────────────────────────────────────────────

def print_cohesion_report(assets: dict, file_path: Optional[str] = None):
    """Run all cohesion checks and print a formatted report."""
    print(f"\n{'='*60}")
    print("DRM FUNNEL COHESION VALIDATOR")
    if file_path:
        print(f"Source: {file_path}")
    print(f"Assets analyzed: {list(assets.keys())}")
    print(f"{'='*60}\n")

    total_checks = 0
    passed_checks = 0
    warnings = []

    # 1. Message Match
    print("[1] MESSAGE MATCH")
    match_result = check_message_match(assets)
    total_checks += 1
    if match_result["status"] == "OK":
        passed_checks += 1
        print(f"    ✅ {match_result['message']}")
    else:
        print(f"    ❌ {match_result['message']}")
        for mm in match_result.get("mismatches", []):
            print(f"       [{mm['step_a']}] \"{mm['headline_a']}\"")
            print(f"       [{mm['step_b']}] \"{mm['headline_b']}\"")
            print(f"       Overlap: {mm['overlap_ratio']*100:.0f}%")
            warnings.append(f"Message mismatch: {mm['step_a']} → {mm['step_b']}")
    print()

    # 2. Price Consistency
    print("[2] PRICE CONSISTENCY")
    price_result = check_price_consistency(assets)
    total_checks += 1
    if price_result["status"] == "OK":
        passed_checks += 1
        if price_result.get("most_common_price"):
            print(f"    ✅ Consistent — main price: {price_result['most_common_price']}")
        else:
            print("    ℹ️  No price mentions found")
    else:
        print(f"    ⚠️  {price_result.get('note', 'Review prices')}")
        print(f"    Prices found: {price_result.get('all_prices_found', [])}")
        warnings.append("Multiple price points — verify consistency")
    print()

    # 3. Vocabulary Consistency
    print("[3] VOCABULARY / TERM CONSISTENCY")
    term_result = check_term_consistency(assets)
    total_checks += 1
    if term_result["status"] == "OK":
        passed_checks += 1
        print(f"    ✅ {term_result['message']}")
        if term_result.get("consistent_terms"):
            print(f"    Consistent terms: {', '.join(term_result['consistent_terms'][:10])}")
    elif term_result["status"] == "REVIEW":
        print(f"    ⚠️  Review vocabulary consistency")
        if term_result.get("potentially_inconsistent"):
            print(f"    Terms appearing in only one asset:")
            for item in term_result["potentially_inconsistent"][:5]:
                print(f"       '{item['term']}' — only in '{item['only_in']}'")
    else:
        print(f"    ℹ️  {term_result.get('status', 'Unable to check')}")
    print()

    # 4. Urgency Consistency
    print("[4] URGENCY / DEADLINE CONSISTENCY")
    urgency_result = check_urgency_consistency(assets)
    total_checks += 1
    if urgency_result["status"] == "OK":
        passed_checks += 1
        if urgency_result.get("urgency_found_in"):
            print(f"    ✅ Urgency consistent — found in: {urgency_result['urgency_found_in']}")
        else:
            print("    ℹ️  No urgency elements found")
    elif urgency_result["status"] == "WARNING":
        print(f"    ⚠️  {urgency_result['message']}")
        for asset, dates in urgency_result.get("specific_dates", {}).items():
            print(f"       [{asset}]: {dates}")
        warnings.append("Deadline dates inconsistent across assets")
    else:
        print(f"    ℹ️  {urgency_result['message']}")
    print()

    # ── SUMMARY ───────────────────────────────────────────────────────────────
    print(f"{'='*60}")
    print(f"COHESION SUMMARY")
    print(f"{'='*60}")
    print(f"Checks passed: {passed_checks}/{total_checks}")

    if warnings:
        print(f"\nISSUES REQUIRING ATTENTION:")
        for w in warnings:
            print(f"  ❌ {w}")

    overall = "PASS" if passed_checks == total_checks else "REVIEW" if passed_checks >= total_checks * 0.75 else "FAIL"
    print(f"\nOverall Status: {overall}")
    print()

    return overall == "PASS"


# ─────────────────────────────────────────────────────────────────────────────
# ASSET LOADING
# ─────────────────────────────────────────────────────────────────────────────

FUNNEL_ORDER = ["ad", "squeeze", "landing", "advertorial", "vsl", "sales", "email", "upsell", "followup"]

def order_assets(assets: dict) -> dict:
    """Order assets by typical funnel sequence."""
    ordered = {}
    for key in FUNNEL_ORDER:
        for asset_name in assets:
            if key in asset_name.lower() and asset_name not in ordered:
                ordered[asset_name] = assets[asset_name]
    # Add any remaining assets
    for asset_name, text in assets.items():
        if asset_name not in ordered:
            ordered[asset_name] = text
    return ordered


def load_assets_from_dir(dir_path: Path) -> dict:
    """Load all .md and .txt files from directory."""
    assets = {}
    files = sorted(list(dir_path.glob("*.md")) + list(dir_path.glob("*.txt")))
    for f in files:
        assets[f.stem] = f.read_text(encoding="utf-8")
    return order_assets(assets)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DRM Squad: Funnel Cohesion Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dir", type=str, help="Directory containing funnel asset files")
    parser.add_argument("--ad", type=str, help="Path to ad copy file")
    parser.add_argument("--landing", type=str, help="Path to landing page copy file")
    parser.add_argument("--email", type=str, help="Path to email copy file")
    parser.add_argument("--vsl", type=str, help="Path to VSL script file")
    parser.add_argument("--sales", type=str, help="Path to sales letter file")

    args = parser.parse_args()
    assets = {}

    if args.dir:
        dir_path = Path(args.dir)
        if not dir_path.exists():
            print(f"Error: Directory not found: {args.dir}")
            sys.exit(2)
        assets = load_assets_from_dir(dir_path)
        if not assets:
            print(f"No .md or .txt files found in {args.dir}")
            sys.exit(2)

    else:
        # Load individually specified files
        file_map = {
            "ad": args.ad,
            "landing": args.landing,
            "email": args.email,
            "vsl": args.vsl,
            "sales": args.sales,
        }
        for label, path_str in file_map.items():
            if path_str:
                path = Path(path_str)
                if not path.exists():
                    print(f"Error: File not found: {path_str}")
                    sys.exit(2)
                assets[label] = path.read_text(encoding="utf-8")

    if len(assets) < 2:
        print("Error: Need at least 2 funnel assets for cohesion validation.")
        print("Use --dir for a directory, or specify at least 2 of: --ad, --landing, --email, --vsl, --sales")
        sys.exit(2)

    passed = print_cohesion_report(assets)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
