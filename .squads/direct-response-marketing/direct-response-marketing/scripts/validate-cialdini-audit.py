#!/usr/bin/env python3
"""
DRM Squad: Cialdini Principles Auditor (Robert Cialdini)
Audits copy for presence and quality of all 7 Principles of Influence.
"Influence is principled. Persuasion is systematic. Apply ethically." — Cialdini

Principles:
    1. Reciprocity       — Give first, obligate second
    2. Commitment        — Small yeses lead to big yeses
    3. Social Proof      — What others do signals correctness
    4. Authority         — Credentials establish credibility
    5. Liking            — Influence from those we like
    6. Scarcity          — Limited availability increases value
    7. Unity             — Shared identity > interpersonal liking

Usage:
    python validate-cialdini-audit.py --file path/to/copy.md
    python validate-cialdini-audit.py --text "Paste copy text here"
    python validate-cialdini-audit.py --file copy.md --strict

    --strict: flags fake/unethical scarcity patterns (RECOMMENDED)

Output:
    - Presence score per principle (0-3)
    - Fake scarcity warnings (ethical filter)
    - Overall Cialdini compliance score
    - Priority recommendations
"""

import argparse
import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# PRINCIPLE SIGNALS
# ─────────────────────────────────────────────────────────────────────────────

PRINCIPLES = {
    1: {
        "name": "Reciprocity",
        "description": "Giving something of value before asking",
        "weight": 10,
        "signals": {
            "free_value": {
                "keywords": ["free", "gift", "bonus", "complimentary", "no charge", "on us",
                             "download", "report", "guide", "checklist", "here's", "giving you"],
                "weight": 40,
            },
            "give_first": {
                "keywords": ["before you decide", "regardless", "even if you don't",
                             "no strings", "no obligation", "keep it", "yours to keep"],
                "weight": 30,
            },
            "advance_value": {
                "keywords": ["tip", "lesson", "secret", "technique", "strategy", "method",
                             "discover", "learn", "find out"],
                "weight": 30,
            },
        },
        "ethical_flag": None,
    },
    2: {
        "name": "Commitment & Consistency",
        "description": "Small agreements leading to larger commitments",
        "weight": 12,
        "signals": {
            "small_ask": {
                "keywords": ["do you want", "are you ready", "are you", "if you", "would you like",
                             "have you ever", "do you believe", "you've already"],
                "weight": 35,
            },
            "identity_anchoring": {
                "keywords": ["you're someone who", "as someone who", "like you", "people like you",
                             "you already know", "you understand", "you care about"],
                "weight": 35,
            },
            "consistency_trigger": {
                "keywords": ["consistent with", "stay true", "follow through", "as you said",
                             "you told me", "you mentioned", "you agreed"],
                "weight": 30,
            },
        },
        "ethical_flag": None,
    },
    3: {
        "name": "Social Proof",
        "description": "Specific evidence of others achieving the result",
        "weight": 18,
        "signals": {
            "specific_testimonial": {
                "patterns": [r'"[^"]{20,}"', r'—\s*[A-Z][a-z]+\s+[A-Z]'],
                "keywords": ["testimonial", "said", "told me", "reported", "shared"],
                "weight": 35,
            },
            "numbers": {
                "patterns": [r'\b\d[\d,]+\s+(?:people|customers|members|students|users|clients)\b',
                              r'\b\d+%\s+(?:of|who|reported|said|achieved)\b'],
                "keywords": [],
                "weight": 35,
            },
            "specificity": {
                "patterns": [r'[A-Z][a-z]+,\s*[A-Z]{2}\b',  # "Jane, FL"
                              r'[A-Z][a-z]+\s+[A-Z][a-z]+,\s*(?:age\s*)?\d{2}'],  # "John Smith, 47"
                "keywords": ["from", "age", "years old", "months ago", "after just"],
                "weight": 30,
            },
        },
        "ethical_flag": None,
    },
    4: {
        "name": "Authority",
        "description": "Credentials established before claims",
        "weight": 15,
        "signals": {
            "credentials": {
                "patterns": [r'\bDr\.?\s+[A-Z]', r'\bPhD\b', r'\bMD\b', r'\bMS\b',
                              r'\bCertified\b', r'\bLicensed\b'],
                "keywords": ["doctor", "professor", "researcher", "studied", "trained",
                             "certified", "licensed", "expert", "specialist"],
                "weight": 35,
            },
            "track_record": {
                "patterns": [r'\$[\d,]+(?:\.\d{2})?\s+(?:in|of|per)', r'\b\d+\s+years?\b'],
                "keywords": ["years of experience", "track record", "helped", "clients",
                             "worked with", "generated", "achieved"],
                "weight": 35,
            },
            "third_party": {
                "patterns": [r'(?:featured in|as seen on|according to)\s+[A-Z]'],
                "keywords": ["featured", "as seen on", "according to", "research shows",
                             "published", "journal", "university", "harvard", "stanford"],
                "weight": 30,
            },
        },
        "ethical_flag": None,
    },
    5: {
        "name": "Liking",
        "description": "Personal connection and shared values established",
        "weight": 10,
        "signals": {
            "similarity": {
                "keywords": ["just like you", "we both", "like me", "like you", "same struggle",
                             "i was where you are", "i understand", "i know how it feels"],
                "weight": 40,
            },
            "personal_story": {
                "keywords": ["i remember", "when i was", "back when", "my story", "personal",
                             "family", "wife", "husband", "kids", "daughter", "son"],
                "weight": 35,
            },
            "warmth": {
                "keywords": ["genuinely", "honestly", "care about", "want to help", "passion",
                             "love", "excited", "believe in"],
                "weight": 25,
            },
        },
        "ethical_flag": None,
    },
    6: {
        "name": "Scarcity",
        "description": "Genuine limited availability — MUST be real",
        "weight": 15,
        "signals": {
            "quantity_limit": {
                "patterns": [r'only\s+\d+\s+(?:spots?|copies|seats|units|packages?)\b',
                              r'\d+\s+(?:spots?|openings?|places?)\s+(?:left|remaining|available)\b'],
                "keywords": ["limited spots", "limited seats", "only accepting",
                             "capacity", "waitlist"],
                "weight": 35,
            },
            "time_limit": {
                "patterns": [r'\b(?:expires?|ends?|closes?)\s+(?:on\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December|\d{1,2}[/-]\d{1,2})',
                              r'(?:midnight|noon)\s+(?:on\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December|\w+day)'],
                "keywords": ["today only", "this week only", "price increases", "doors close",
                             "enrollment closes"],
                "weight": 35,
            },
            "reason_given": {
                "keywords": ["because", "due to", "the reason", "why we limit",
                             "we can only", "to maintain quality", "production capacity"],
                "weight": 30,
            },
        },
        "ethical_flag": {
            "fake_patterns": [
                (r'\btoday only\b.*\btoday only\b', "Repeated 'today only' — likely evergreen fake scarcity"),
                (r'(?:limited time|expires soon|hurry)[^.]{0,100}(?:limited time|expires soon|hurry)', "Duplicate urgency phrases — may be template-generated"),
                (r'\blimited spots\b[^.!?]{0,200}\ball slots filled\b', "Contradictory scarcity claims"),
                (r'(?:act now|hurry)\s*!{2,}', "Multiple exclamation marks on urgency — hallmark of fake urgency"),
            ],
            "warning_message": "ETHICAL FLAG: Cialdini Rule — scarcity MUST be real. Fake urgency destroys trust.",
        },
    },
    7: {
        "name": "Unity",
        "description": "Shared identity beyond mere liking — we/us framing",
        "weight": 10,
        "signals": {
            "shared_identity": {
                "keywords": ["we are", "one of us", "our community", "our tribe", "people like us",
                             "members of", "belong to", "part of something", "movement"],
                "weight": 40,
            },
            "family_metaphor": {
                "keywords": ["family", "together", "our journey", "join us", "side by side",
                             "in this together", "community", "mission"],
                "weight": 35,
            },
            "values_alignment": {
                "keywords": ["believe", "stand for", "against", "fight for", "committed to",
                             "our values", "principles", "mission"],
                "weight": 25,
            },
        },
        "ethical_flag": None,
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# SCORING FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def score_principle(text: str, principle: dict) -> dict:
    """Score a single Cialdini principle presence in the text."""
    text_lower = text.lower()
    total_weight = 0
    earned_weight = 0
    component_results = {}

    for signal_id, signal in principle["signals"].items():
        weight = signal["weight"]
        total_weight += weight
        found = False

        if "patterns" in signal:
            for pattern in signal["patterns"]:
                if re.search(pattern, text, re.IGNORECASE):
                    found = True
                    break

        if not found and "keywords" in signal:
            for keyword in signal["keywords"]:
                if keyword.lower() in text_lower:
                    found = True
                    break

        if found:
            earned_weight += weight

        component_results[signal_id] = {"found": found, "weight": weight}

    raw_score = earned_weight / total_weight if total_weight > 0 else 0
    # Map to 0-3 scale: 0 = absent, 1 = weak, 2 = moderate, 3 = strong
    if raw_score >= 0.75:
        level = 3
    elif raw_score >= 0.45:
        level = 2
    elif raw_score >= 0.15:
        level = 1
    else:
        level = 0

    return {
        "level": level,
        "raw_score": round(raw_score, 2),
        "components": component_results,
        "earned": earned_weight,
        "total": total_weight,
    }


def check_ethical_flags(text: str, principle_num: int, principle: dict) -> list:
    """Check for unethical/fake persuasion patterns."""
    flags = []
    ethical_flag = principle.get("ethical_flag")
    if not ethical_flag:
        return flags

    for pattern, message in ethical_flag.get("fake_patterns", []):
        if re.search(pattern, text, re.IGNORECASE):
            flags.append(message)

    return flags


# ─────────────────────────────────────────────────────────────────────────────
# REPORTING
# ─────────────────────────────────────────────────────────────────────────────

LEVEL_LABELS = {0: "ABSENT", 1: "WEAK", 2: "MODERATE", 3: "STRONG"}
LEVEL_ICONS = {0: "❌", 1: "⚠️", 2: "🟡", 3: "✅"}
LEVEL_SCORES = {0: 0, 1: 33, 2: 67, 3: 100}

BAR_CHARS = {0: "░░░", 1: "█░░", 2: "██░", 3: "███"}


def print_cialdini_report(text: str, file_name: str = "copy", strict: bool = False):
    """Run Cialdini audit and print formatted report."""
    print(f"\n{'='*60}")
    print("DRM SQUAD: CIALDINI PRINCIPLES AUDIT")
    print(f"File: {file_name}")
    print(f"Word count: {len(text.split())} words")
    if strict:
        print("Mode: STRICT (ethical filter enabled)")
    print(f"{'='*60}\n")

    principle_results = {}
    all_ethical_flags = []
    total_weighted_score = 0
    total_weight = 0

    for num, principle in PRINCIPLES.items():
        result = score_principle(text, principle)
        ethical_flags = check_ethical_flags(text, num, principle) if strict else []
        principle_results[num] = {**result, "flags": ethical_flags}
        all_ethical_flags.extend(ethical_flags)

        weight = principle["weight"]
        total_weight += weight
        total_weighted_score += LEVEL_SCORES[result["level"]] * weight

    # ── PRINCIPLE SCORECARD ──────────────────────────────────────────────────
    print("PRINCIPLE SCORECARD")
    print(f"  {'#':<3} {'Principle':<25} {'Level':<12} {'Bar':<8} {'Score'}")
    print(f"  {'-'*3} {'-'*25} {'-'*12} {'-'*8} {'-'*5}")

    for num, result in principle_results.items():
        principle = PRINCIPLES[num]
        level = result["level"]
        icon = LEVEL_ICONS[level]
        label = LEVEL_LABELS[level]
        bar = BAR_CHARS[level]
        score = LEVEL_SCORES[level]
        print(f"  {num:<3} {principle['name']:<25} {icon} {label:<10} {bar}  {score}/100")

    print()

    # ── PRINCIPLE DETAIL ─────────────────────────────────────────────────────
    print("PRINCIPLE DETAIL")
    for num, result in principle_results.items():
        principle = PRINCIPLES[num]
        level = result["level"]
        icon = LEVEL_ICONS[level]
        print(f"\n  [{num}] {principle['name']} — {LEVEL_LABELS[level]}")
        print(f"  Description: {principle['description']}")

        missing = [sid for sid, r in result["components"].items() if not r["found"]]
        present = [sid for sid, r in result["components"].items() if r["found"]]

        if present:
            print(f"  ✅ Found: {', '.join(present)}")
        if missing:
            print(f"  ❌ Missing: {', '.join(missing)}")

        if result["flags"]:
            print(f"  ⛔ ETHICAL FLAGS:")
            for flag in result["flags"]:
                print(f"     → {flag}")

    print()

    # ── ETHICAL FLAGS SUMMARY ────────────────────────────────────────────────
    if strict:
        print("ETHICAL AUDIT (Cialdini Standard: Only real scarcity)")
        if all_ethical_flags:
            print("  ⛔ VIOLATIONS DETECTED:")
            for flag in all_ethical_flags:
                print(f"  → {flag}")
            print(f"\n  ⚠️  {PRINCIPLES[6]['ethical_flag']['warning_message']}")
        else:
            print("  ✅ No unethical persuasion patterns detected")
        print()

    # ── COVERAGE ANALYSIS ────────────────────────────────────────────────────
    absent = [PRINCIPLES[n]["name"] for n, r in principle_results.items() if r["level"] == 0]
    weak = [PRINCIPLES[n]["name"] for n, r in principle_results.items() if r["level"] == 1]
    strong = [PRINCIPLES[n]["name"] for n, r in principle_results.items() if r["level"] >= 2]

    print("COVERAGE ANALYSIS")
    print(f"  Strong/Moderate: {len(strong)}/7 principles well-represented")
    print(f"  Weak: {len(weak)} — {', '.join(weak) if weak else 'none'}")
    print(f"  Absent: {len(absent)} — {', '.join(absent) if absent else 'none'}")
    print()

    # ── OVERALL SCORE ────────────────────────────────────────────────────────
    overall = int(total_weighted_score / total_weight) if total_weight > 0 else 0
    # Penalize for ethical flags
    overall = max(0, overall - (len(all_ethical_flags) * 10))

    print(f"{'='*60}")
    grade = "FULL INFLUENCE STACK" if overall >= 80 else "GOOD" if overall >= 65 else "PARTIAL" if overall >= 45 else "WEAK"
    print(f"CIALDINI COMPLIANCE SCORE: {overall}/100 — {grade}")
    print(f"Principles used: {7 - len(absent)}/7")
    print(f"{'='*60}")

    # Priority recommendations
    if absent or weak:
        print("\nPRIORITY ADDITIONS (highest impact first):")
        priority_order = sorted(
            [(n, r) for n, r in principle_results.items() if r["level"] <= 1],
            key=lambda x: PRINCIPLES[x[0]]["weight"],
            reverse=True,
        )
        for num, result in priority_order[:3]:
            principle = PRINCIPLES[num]
            missing_signals = [sid for sid, r in result["components"].items() if not r["found"]]
            print(f"  [{num}] {principle['name']} (weight: {principle['weight']})")
            print(f"      Add: {principle['description']}")
            if missing_signals:
                print(f"      Missing signals: {', '.join(missing_signals[:2])}")

    print()
    return overall


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DRM Squad: Cialdini 7 Principles Auditor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to copy file (.md or .txt)")
    group.add_argument("--text", type=str, help="Raw copy text to analyze")

    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable ethical filter (flags fake/unethical scarcity patterns)",
    )

    args = parser.parse_args()

    if args.text:
        score = print_cialdini_report(args.text, "inline text", strict=args.strict)
    else:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File not found: {args.file}")
            sys.exit(2)
        text = file_path.read_text(encoding="utf-8")
        score = print_cialdini_report(text, file_path.name, strict=args.strict)

    sys.exit(0 if score >= 65 else 1)


if __name__ == "__main__":
    main()
