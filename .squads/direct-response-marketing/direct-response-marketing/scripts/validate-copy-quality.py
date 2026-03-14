#!/usr/bin/env python3
"""
DRM Squad: Copy Quality Validator
Validates copy assets against Gary Halbert's specificity standards
and DRM quality benchmarks.

Usage:
    python validate-copy-quality.py --file path/to/copy.md
    python validate-copy-quality.py --dir path/to/copy/assets/
    python validate-copy-quality.py --text "Paste copy here directly"

Output:
    - Specificity ratio score
    - Vague language flags
    - Missing structural elements
    - Quality score out of 100
"""

import argparse
import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

VAGUE_WORDS = [
    "many", "several", "some", "few", "numerous", "various", "multiple",
    "amazing", "incredible", "unbelievable", "powerful", "revolutionary",
    "best", "ultimate", "greatest", "perfect", "awesome", "fantastic",
    "quickly", "soon", "fast", "rapidly", "instantly", "immediately",
    "thousands", "millions", "hundreds",  # vague if not preceded by specific number
    "everyone", "nobody", "always", "never",
    "results may vary", "typical results",
    "proven", "guaranteed",  # vague if not followed by specific claim
]

SPECIFIC_PATTERNS = [
    r'\b\d+\s*(?:people|customers|clients|students|members|users)\b',  # "4,231 customers"
    r'\$\d[\d,]*(?:\.\d{2})?',  # "$1,297.00" or "$47"
    r'\b\d+\s*(?:days?|weeks?|months?|hours?|minutes?|years?)\b',  # "14 days"
    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,?\s*\d{4}\b',  # specific dates
    r'\b\d+%\b',  # percentages
    r'\b\d+x\b',  # multipliers like "10x"
    r'[A-Z][a-z]+\s+[A-Z][a-z]+(?:,\s+[A-Z][a-z]+(?:,\s+[A-Z]{2})?)?',  # full names
]

REQUIRED_COPY_ELEMENTS = {
    "headline": {
        "patterns": [r'^#{1,2}\s+.+', r'^[A-Z].{20,}$'],
        "description": "Headline/opening hook",
        "weight": 15,
    },
    "problem_identification": {
        "keywords": ["problem", "struggle", "frustrat", "stuck", "fail", "can't", "difficult", "challenge"],
        "description": "Problem identification section",
        "weight": 10,
    },
    "mechanism": {
        "keywords": ["because", "reason", "secret", "discover", "method", "system", "formula", "process", "how"],
        "description": "Mechanism explanation",
        "weight": 15,
    },
    "social_proof": {
        "patterns": [r'"[^"]{20,}"', r'—\s*[A-Z][a-z]+\s+[A-Z][a-z]+'],
        "keywords": ["testimonial", "client", "customer", "said", "told me", "results"],
        "description": "Social proof / testimonials",
        "weight": 15,
    },
    "cta": {
        "keywords": ["click", "download", "get", "start", "join", "order", "call", "visit", "go to", "sign up", "register"],
        "description": "Call to action",
        "weight": 20,
    },
    "guarantee": {
        "keywords": ["guarantee", "refund", "risk", "protected", "assured", "promise"],
        "description": "Guarantee or risk reversal",
        "weight": 10,
    },
    "urgency": {
        "keywords": ["today", "now", "limited", "expires", "deadline", "soon", "hurry", "before"],
        "description": "Urgency element",
        "weight": 15,
    },
}

FORBIDDEN_OPENERS = [
    "hi, i'm",
    "my name is",
    "we are",
    "we're",
    "welcome to",
    "i want to",
    "i would like",
    "thank you for",
    "congratulations",
    "i hope this finds you",
    "i'm writing to",
]


# ─────────────────────────────────────────────────────────────────────────────
# ANALYSIS FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def calculate_specificity_ratio(text: str) -> dict:
    """
    Calculate the ratio of specific claims vs. vague claims.
    Gary Halbert standard: aim for 80%+ specificity.
    """
    words = text.lower().split()
    total_words = len(words)

    # Count specific claims
    specific_count = 0
    specific_examples = []
    for pattern in SPECIFIC_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        specific_count += len(matches)
        specific_examples.extend(matches[:3])  # Show first 3 examples

    # Count vague words
    vague_count = 0
    vague_found = []
    for word in VAGUE_WORDS:
        occurrences = len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE))
        if occurrences > 0:
            vague_count += occurrences
            vague_found.append(f"{word} (x{occurrences})")

    # Normalize to ratio
    if specific_count + vague_count == 0:
        ratio = 0.5
    else:
        ratio = specific_count / (specific_count + vague_count)

    return {
        "ratio": ratio,
        "percentage": int(ratio * 100),
        "specific_count": specific_count,
        "vague_count": vague_count,
        "specific_examples": specific_examples[:5],
        "vague_words_found": vague_found,
        "rating": "EXCELLENT" if ratio >= 0.8 else "GOOD" if ratio >= 0.6 else "NEEDS WORK" if ratio >= 0.4 else "POOR",
    }


def check_forbidden_opener(text: str) -> dict:
    """
    Check if copy opens with a forbidden pattern.
    Gary Halbert/Ryan Deiss rule: Never open with company name or "Hi, I'm..."
    """
    first_200 = text[:200].lower().strip()

    for opener in FORBIDDEN_OPENERS:
        if first_200.startswith(opener):
            return {
                "failed": True,
                "found": opener,
                "message": f"Copy opens with forbidden phrase: '{opener}'"
            }

    return {"failed": False}


def check_required_elements(text: str) -> dict:
    """
    Check for presence of required copy structural elements.
    """
    text_lower = text.lower()
    results = {}
    total_weight = 0
    earned_weight = 0

    for element_id, config in REQUIRED_COPY_ELEMENTS.items():
        weight = config["weight"]
        total_weight += weight
        found = False

        # Check patterns
        if "patterns" in config:
            for pattern in config["patterns"]:
                if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
                    found = True
                    break

        # Check keywords
        if not found and "keywords" in config:
            for keyword in config["keywords"]:
                if keyword in text_lower:
                    found = True
                    break

        if found:
            earned_weight += weight

        results[element_id] = {
            "found": found,
            "description": config["description"],
            "weight": weight,
        }

    score = int((earned_weight / total_weight) * 100) if total_weight > 0 else 0

    return {
        "elements": results,
        "score": score,
        "earned_weight": earned_weight,
        "total_weight": total_weight,
    }


def check_passive_voice(text: str) -> dict:
    """
    Flag excessive passive voice usage.
    """
    passive_patterns = [
        r'\bcan be\b', r'\bwill be\b', r'\bis being\b', r'\bwas\b.*\bby\b',
        r'\bhas been\b', r'\bhave been\b', r'\bare being\b', r'\bwere being\b',
        r'\bshould be\b', r'\bcould be\b', r'\bmight be\b', r'\bwould be\b',
    ]

    passive_count = 0
    passive_examples = []
    for pattern in passive_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        passive_count += len(matches)
        if matches:
            passive_examples.extend(matches[:2])

    # Get approximate sentence count for ratio
    sentences = len(re.findall(r'[.!?]+', text))
    ratio = passive_count / max(sentences, 1)

    return {
        "passive_count": passive_count,
        "sentence_count": sentences,
        "ratio": round(ratio, 2),
        "examples": list(set(passive_examples))[:5],
        "status": "OK" if ratio < 0.1 else "WARNING" if ratio < 0.2 else "HIGH",
    }


def check_you_vs_we(text: str) -> dict:
    """
    Frank Kern rule: 'You' must appear more than 'I' or 'We'.
    """
    text_lower = text.lower()
    you_count = len(re.findall(r'\byou\b|\byour\b|\byours\b', text_lower))
    we_count = len(re.findall(r'\bwe\b|\bour\b|\bours\b', text_lower))
    i_count = len(re.findall(r'\bi\b|\bme\b|\bmy\b|\bmine\b', text_lower))

    seller_count = we_count + i_count
    ratio = you_count / max(seller_count, 1)

    return {
        "you_count": you_count,
        "seller_count": seller_count,
        "ratio": round(ratio, 2),
        "status": "GOOD" if ratio >= 1.5 else "WARNING" if ratio >= 1.0 else "POOR",
        "note": "Target: 'You' appears at least 1.5x more than I/We",
    }


def calculate_readability(text: str) -> dict:
    """
    Basic readability assessment.
    """
    words = text.split()
    sentences = len(re.findall(r'[.!?]+', text)) or 1
    paragraphs = len([p for p in text.split('\n\n') if p.strip()])

    avg_sentence_length = len(words) / sentences
    avg_paragraph_length = sentences / max(paragraphs, 1)

    return {
        "word_count": len(words),
        "sentence_count": sentences,
        "paragraph_count": paragraphs,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_paragraph_length": round(avg_paragraph_length, 1),
        "sentence_length_status": "OK" if avg_sentence_length < 20 else "WARNING",
        "paragraph_status": "OK" if avg_paragraph_length < 4 else "WARNING",
    }


# ─────────────────────────────────────────────────────────────────────────────
# SCORING
# ─────────────────────────────────────────────────────────────────────────────

def calculate_overall_score(specificity: dict, elements: dict, passive: dict,
                             you_vs_we: dict, forbidden_opener: dict) -> int:
    """Calculate weighted overall quality score out of 100."""
    score = 0

    # Specificity (30 points)
    score += int(specificity["ratio"] * 30)

    # Structural elements (40 points)
    score += int(elements["score"] * 0.4)

    # Passive voice (10 points)
    if passive["status"] == "OK":
        score += 10
    elif passive["status"] == "WARNING":
        score += 5

    # You vs We balance (10 points)
    if you_vs_we["status"] == "GOOD":
        score += 10
    elif you_vs_we["status"] == "WARNING":
        score += 5

    # Forbidden opener (10 points)
    if not forbidden_opener["failed"]:
        score += 10

    return min(score, 100)


# ─────────────────────────────────────────────────────────────────────────────
# REPORTING
# ─────────────────────────────────────────────────────────────────────────────

def print_report(text: str, file_name: str = "copy"):
    """Run all checks and print a formatted report."""
    print(f"\n{'='*60}")
    print(f"DRM COPY QUALITY VALIDATOR")
    print(f"File: {file_name}")
    print(f"{'='*60}\n")

    # Run all checks
    specificity = calculate_specificity_ratio(text)
    forbidden = check_forbidden_opener(text)
    elements = check_required_elements(text)
    passive = check_passive_voice(text)
    you_vs_we = check_you_vs_we(text)
    readability = calculate_readability(text)
    overall_score = calculate_overall_score(specificity, elements, passive, you_vs_we, forbidden)

    # ── SPECIFICITY ──────────────────────────────────────────────────────────
    print(f"[1] SPECIFICITY (Gary Halbert Standard)")
    print(f"    Score: {specificity['percentage']}% — {specificity['rating']}")
    print(f"    Specific claims found: {specificity['specific_count']}")
    print(f"    Vague instances found: {specificity['vague_count']}")
    if specificity['vague_words_found']:
        print(f"    Vague words: {', '.join(specificity['vague_words_found'][:8])}")
    if specificity['specific_examples']:
        print(f"    Specific examples: {specificity['specific_examples'][:3]}")
    print()

    # ── OPENING ──────────────────────────────────────────────────────────────
    print(f"[2] OPENING CHECK")
    if forbidden["failed"]:
        print(f"    ❌ FAILED: {forbidden['message']}")
    else:
        print(f"    ✅ PASSED: Copy does not open with a forbidden phrase")
    print()

    # ── STRUCTURAL ELEMENTS ───────────────────────────────────────────────────
    print(f"[3] STRUCTURAL ELEMENTS")
    print(f"    Score: {elements['score']}/100")
    for elem_id, result in elements["elements"].items():
        status = "✅" if result["found"] else "❌"
        print(f"    {status} {result['description']} (weight: {result['weight']})")
    print()

    # ── PASSIVE VOICE ─────────────────────────────────────────────────────────
    print(f"[4] PASSIVE VOICE")
    status_icon = "✅" if passive["status"] == "OK" else "⚠️" if passive["status"] == "WARNING" else "❌"
    print(f"    {status_icon} {passive['status']}: {passive['passive_count']} passive constructions / {passive['sentence_count']} sentences")
    if passive["examples"]:
        print(f"    Examples: {passive['examples'][:3]}")
    print()

    # ── YOU VS WE ─────────────────────────────────────────────────────────────
    print(f"[5] BUYER-FOCUSED LANGUAGE (You vs I/We)")
    status_icon = "✅" if you_vs_we["status"] == "GOOD" else "⚠️" if you_vs_we["status"] == "WARNING" else "❌"
    print(f"    {status_icon} {you_vs_we['status']}: You={you_vs_we['you_count']} vs I/We={you_vs_we['seller_count']} (ratio: {you_vs_we['ratio']})")
    print()

    # ── READABILITY ───────────────────────────────────────────────────────────
    print(f"[6] READABILITY")
    print(f"    Word count: {readability['word_count']}")
    sl_icon = "✅" if readability["sentence_length_status"] == "OK" else "⚠️"
    print(f"    {sl_icon} Avg sentence length: {readability['avg_sentence_length']} words")
    para_icon = "✅" if readability["paragraph_status"] == "OK" else "⚠️"
    print(f"    {para_icon} Avg paragraph length: {readability['avg_paragraph_length']} sentences")
    print()

    # ── OVERALL SCORE ─────────────────────────────────────────────────────────
    print(f"{'='*60}")
    grade = "EXCELLENT" if overall_score >= 85 else "GOOD" if overall_score >= 70 else "NEEDS WORK" if overall_score >= 55 else "POOR"
    print(f"OVERALL QUALITY SCORE: {overall_score}/100 — {grade}")
    print(f"{'='*60}\n")

    # Recommendations
    if overall_score < 85:
        print("RECOMMENDATIONS:")
        if specificity["ratio"] < 0.7:
            print("  → Replace vague words with specific numbers, names, and dates")
        if forbidden["failed"]:
            print(f"  → Rewrite opener — remove '{forbidden['found']}'")
        for elem_id, result in elements["elements"].items():
            if not result["found"]:
                print(f"  → Add missing element: {result['description']}")
        if passive["status"] != "OK":
            print("  → Rewrite passive constructions to active voice")
        if you_vs_we["status"] != "GOOD":
            print("  → Increase 'you/your' and reduce 'we/our/I' throughout copy")
        print()

    return overall_score


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DRM Squad: Copy Quality Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to copy file (.md or .txt)")
    group.add_argument("--dir", type=str, help="Directory with multiple copy files")
    group.add_argument("--text", type=str, help="Raw copy text to analyze")

    args = parser.parse_args()

    if args.text:
        score = print_report(args.text, "inline text")
        sys.exit(0 if score >= 70 else 1)

    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File not found: {args.file}")
            sys.exit(2)
        text = file_path.read_text(encoding="utf-8")
        score = print_report(text, file_path.name)
        sys.exit(0 if score >= 70 else 1)

    elif args.dir:
        dir_path = Path(args.dir)
        if not dir_path.exists():
            print(f"Error: Directory not found: {args.dir}")
            sys.exit(2)

        files = list(dir_path.glob("*.md")) + list(dir_path.glob("*.txt"))
        if not files:
            print(f"No .md or .txt files found in {args.dir}")
            sys.exit(2)

        scores = []
        for f in sorted(files):
            text = f.read_text(encoding="utf-8")
            score = print_report(text, f.name)
            scores.append((f.name, score))

        print(f"\n{'='*60}")
        print("BATCH SUMMARY")
        print(f"{'='*60}")
        for name, score in sorted(scores, key=lambda x: x[1], reverse=True):
            grade = "✅" if score >= 70 else "⚠️" if score >= 55 else "❌"
            print(f"  {grade} {name}: {score}/100")
        avg = sum(s for _, s in scores) / len(scores)
        print(f"\nAverage score: {avg:.1f}/100")
        print(f"Files analyzed: {len(files)}")

        failed = [name for name, score in scores if score < 70]
        sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
