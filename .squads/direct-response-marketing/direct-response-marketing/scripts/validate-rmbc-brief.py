#!/usr/bin/env python3
"""
DRM Squad: RMBC Brief Validator (Stefan Georgi)
Validates a copy brief against the RMBC Method standards.
"Great copy isn't written — it's assembled." — Stefan Georgi

RMBC = Research → Mechanism → Brief → Copy
The Brief is the architecture before writing. Without it, copy fails.

Usage:
    python validate-rmbc-brief.py --file path/to/brief.md
    python validate-rmbc-brief.py --text "Paste brief content here"

Output:
    - Phase-by-phase completeness scores
    - Missing components
    - Overall RMBC brief score out of 100
    - Specific recommendations before writing
"""

import argparse
import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# RMBC PHASE CHECKS
# ─────────────────────────────────────────────────────────────────────────────

# Phase 1: Research completeness signals
RESEARCH_SIGNALS = {
    "avatar_defined": {
        "keywords": ["avatar", "prospect", "customer", "buyer", "who is", "target"],
        "description": "Avatar / target prospect defined",
        "weight": 15,
    },
    "frustrations_captured": {
        "keywords": ["frustrat", "struggl", "pain", "fear", "worry", "hate", "tired of", "sick of", "annoyed"],
        "description": "Frustrations / pain points documented",
        "weight": 15,
    },
    "desires_captured": {
        "keywords": ["want", "desire", "dream", "goal", "wish", "hope", "ideal", "imagine", "finally"],
        "description": "Desires / aspirations documented",
        "weight": 10,
    },
    "voc_present": {
        "patterns": [r'"[^"]{15,}"', r"'[^']{15,}'"],
        "keywords": ["verbatim", "quote", "said", "wrote", "review", "forum", "reddit", "amazon"],
        "description": "Voice-of-customer (VOC) phrases or sources referenced",
        "weight": 20,
    },
    "market_sophistication": {
        "keywords": ["awareness", "stage", "sophistication", "level", "market", "cold", "warm", "hot"],
        "description": "Market awareness / sophistication stage noted",
        "weight": 10,
    },
    "objections_listed": {
        "keywords": ["objection", "concern", "doubt", "hesit", "worry", "skeptic", "but what about", "what if"],
        "description": "Key objections / skepticisms listed",
        "weight": 15,
    },
    "beliefs_documented": {
        "keywords": ["believe", "think", "assume", "currently", "already tried", "they think", "they believe"],
        "description": "Current false beliefs or prior attempts documented",
        "weight": 15,
    },
}

# Phase 2: Mechanism definition signals
MECHANISM_SIGNALS = {
    "mechanism_named": {
        "patterns": [r'\b[A-Z][a-z]+ [A-Z][a-z]+\b.*(?:method|system|formula|protocol|process|framework)',
                     r'(?:the|our|my)\s+[A-Z][a-zA-Z]+\s+(?:Method|System|Formula|Process|Protocol)'],
        "keywords": ["mechanism", "method", "system", "formula", "process", "secret", "breakthrough",
                     "proprietary", "unique", "named", "called"],
        "description": "Mechanism is named (has a specific, proprietary name)",
        "weight": 25,
    },
    "mechanism_type": {
        "keywords": ["ingredient", "process", "discovery", "reversal", "elimination",
                     "compound", "combines", "unlike", "instead of"],
        "description": "Mechanism type identified (ingredient/process/discovery/reversal/elimination)",
        "weight": 15,
    },
    "why_it_works": {
        "keywords": ["because", "reason", "science", "research", "studies", "proven", "explains why",
                     "the reason", "this works by", "how it works"],
        "description": "Explanation of WHY mechanism works (logical proof)",
        "weight": 20,
    },
    "mechanism_specific": {
        "patterns": [r'\b\d+\s*(?:steps?|phases?|stages?|elements?|components?|ingredients?)\b',
                     r'\b\d+%\b', r'\b\d+x\b'],
        "keywords": ["specific", "exact", "precise", "particular", "step-by-step"],
        "description": "Mechanism is specific (not generic/vague)",
        "weight": 20,
    },
    "differentiation": {
        "keywords": ["unlike", "different from", "unlike other", "not like", "while others",
                     "most solutions", "traditional approach", "what makes this different"],
        "description": "Differentiation from existing solutions stated",
        "weight": 20,
    },
}

# Phase 3: Brief completeness (the 7 required components)
BRIEF_COMPONENTS = {
    "avatar_summary": {
        "keywords": ["avatar:", "prospect:", "target:", "who:", "audience:"],
        "patterns": [r'(?:^|\n)#+\s*Avatar', r'(?:^|\n)#+\s*Target', r'(?:^|\n)#+\s*Prospect'],
        "description": "Avatar summary section",
        "weight": 10,
    },
    "mechanism_summary": {
        "keywords": ["mechanism:", "the mechanism", "core mechanism"],
        "patterns": [r'(?:^|\n)#+\s*Mechanism'],
        "description": "Mechanism summary (what it is and why it works)",
        "weight": 15,
    },
    "hook_options": {
        "keywords": ["hook", "headline", "opening", "angle", "lead", "option 1", "option 2", "hook 1", "hook 2"],
        "patterns": [r'(?:^|\n)#+\s*Hook', r'(?:^|\n)#+\s*Headline'],
        "description": "Hook / headline options (minimum 3)",
        "weight": 15,
    },
    "story_outline": {
        "keywords": ["story", "origin", "backstory", "journey", "narrative", "how i discovered",
                     "how they found", "turning point"],
        "patterns": [r'(?:^|\n)#+\s*Story'],
        "description": "Story / origin narrative outlined",
        "weight": 15,
    },
    "proof_inventory": {
        "keywords": ["proof", "testimonial", "case study", "before/after", "result", "evidence",
                     "study", "research", "data"],
        "patterns": [r'(?:^|\n)#+\s*Proof', r'(?:^|\n)#+\s*Evidence', r'(?:^|\n)#+\s*Social Proof'],
        "description": "Proof inventory (testimonials, data, case studies listed)",
        "weight": 15,
    },
    "offer_structure": {
        "keywords": ["offer", "price", "bonus", "value", "guarantee", "include", "get", "receive",
                     "what they get", "$"],
        "patterns": [r'(?:^|\n)#+\s*Offer', r'\$\d+'],
        "description": "Offer structure (price, bonuses, guarantee outlined)",
        "weight": 15,
    },
    "cta_approach": {
        "keywords": ["call to action", "cta", "close", "next step", "order", "click", "buy now",
                     "urgency", "deadline", "scarcity", "limited"],
        "patterns": [r'(?:^|\n)#+\s*CTA', r'(?:^|\n)#+\s*Close'],
        "description": "CTA / close approach defined (urgency mechanism specified)",
        "weight": 15,
    },
}

# Red flags that indicate weak brief
RED_FLAGS = [
    (r'\bTBD\b', "TBD found — brief incomplete"),
    (r'\bTK\b', "TK placeholder found — brief incomplete"),
    (r'\bFILL IN\b', "Fill-in placeholder found"),
    (r'\[INSERT\]', "INSERT placeholder found"),
    (r'\bN/A\b', "N/A found — skipped section"),
    (r'\.{3,}', "Ellipsis placeholder found — may indicate skipped content"),
]


# ─────────────────────────────────────────────────────────────────────────────
# SCORING FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def score_phase(text: str, signals: dict) -> dict:
    """Score a phase by checking presence of required signals."""
    text_lower = text.lower()
    results = {}
    total_weight = 0
    earned_weight = 0

    for signal_id, config in signals.items():
        weight = config["weight"]
        total_weight += weight
        found = False

        if "patterns" in config:
            for pattern in config["patterns"]:
                if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
                    found = True
                    break

        if not found and "keywords" in config:
            for keyword in config["keywords"]:
                if keyword.lower() in text_lower:
                    found = True
                    break

        if found:
            earned_weight += weight

        results[signal_id] = {
            "found": found,
            "description": config["description"],
            "weight": weight,
        }

    score = int((earned_weight / total_weight) * 100) if total_weight > 0 else 0
    return {
        "components": results,
        "score": score,
        "earned": earned_weight,
        "total": total_weight,
    }


def check_red_flags(text: str) -> list:
    """Check for placeholder/incomplete brief markers."""
    flags = []
    for pattern, message in RED_FLAGS:
        if re.search(pattern, text, re.IGNORECASE):
            flags.append(message)
    return flags


def count_hook_options(text: str) -> int:
    """Count the number of hook/headline options in the brief."""
    patterns = [
        r'(?:hook|headline|angle)\s*(?:#?\d+|[Aa]|[Bb]|[Cc]|option)',
        r'(?:option|version|variant)\s*(?:#?\d+|[Aa]|[Bb]|[Cc])',
        r'^\s*[-*]\s+(?:hook|headline)',
    ]
    count = 0
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        count = max(count, len(matches))
    return count


# ─────────────────────────────────────────────────────────────────────────────
# REPORTING
# ─────────────────────────────────────────────────────────────────────────────

def print_rmbc_report(text: str, file_name: str = "brief"):
    """Run all RMBC checks and print a formatted report."""
    print(f"\n{'='*60}")
    print("DRM SQUAD: RMBC BRIEF VALIDATOR (Stefan Georgi)")
    print(f"File: {file_name}")
    print(f"Word count: {len(text.split())} words")
    print(f"{'='*60}\n")

    # Run phase checks
    research = score_phase(text, RESEARCH_SIGNALS)
    mechanism = score_phase(text, MECHANISM_SIGNALS)
    brief = score_phase(text, BRIEF_COMPONENTS)
    red_flags = check_red_flags(text)
    hook_count = count_hook_options(text)

    # ── PHASE 1: RESEARCH ────────────────────────────────────────────────────
    print("[PHASE 1] RESEARCH (target: 80%+)")
    print(f"    Score: {research['score']}/100")
    for sid, result in research["components"].items():
        icon = "✅" if result["found"] else "❌"
        print(f"    {icon} {result['description']} (weight: {result['weight']})")
    print()

    # ── PHASE 2: MECHANISM ───────────────────────────────────────────────────
    print("[PHASE 2] MECHANISM (target: 80%+)")
    print(f"    Score: {mechanism['score']}/100")
    for sid, result in mechanism["components"].items():
        icon = "✅" if result["found"] else "❌"
        print(f"    {icon} {result['description']} (weight: {result['weight']})")
    print()

    # ── PHASE 3: BRIEF ───────────────────────────────────────────────────────
    print("[PHASE 3] BRIEF COMPONENTS (all 7 required)")
    print(f"    Score: {brief['score']}/100")
    for sid, result in brief["components"].items():
        icon = "✅" if result["found"] else "❌"
        print(f"    {icon} {result['description']} (weight: {result['weight']})")

    # Hook count sub-check
    hook_icon = "✅" if hook_count >= 3 else "⚠️" if hook_count >= 1 else "❌"
    print(f"\n    {hook_icon} Hook options detected: {hook_count} (minimum 3 required)")
    print()

    # ── RED FLAGS ────────────────────────────────────────────────────────────
    print("[RED FLAGS] Incomplete Brief Indicators")
    if red_flags:
        for flag in red_flags:
            print(f"    ❌ {flag}")
    else:
        print("    ✅ No incomplete brief placeholders found")
    print()

    # ── OVERALL SCORE ────────────────────────────────────────────────────────
    # Weighted: Research 30%, Mechanism 35%, Brief 35%
    overall = int(research["score"] * 0.30 + mechanism["score"] * 0.35 + brief["score"] * 0.35)
    # Penalize for red flags
    overall = max(0, overall - (len(red_flags) * 5))

    print(f"{'='*60}")
    grade = "READY TO WRITE" if overall >= 80 else "NEEDS WORK" if overall >= 60 else "DO NOT WRITE YET"
    print(f"OVERALL RMBC BRIEF SCORE: {overall}/100 — {grade}")
    print(f"{'='*60}")

    if overall < 80:
        print("\nBLOCKERS (fix before writing copy):")
        if research["score"] < 70:
            for sid, r in research["components"].items():
                if not r["found"]:
                    print(f"  → Research: Add '{r['description']}'")
        if mechanism["score"] < 70:
            for sid, r in mechanism["components"].items():
                if not r["found"]:
                    print(f"  → Mechanism: Complete '{r['description']}'")
        if brief["score"] < 70:
            for sid, r in brief["components"].items():
                if not r["found"]:
                    print(f"  → Brief: Add section for '{r['description']}'")
        if hook_count < 3:
            print(f"  → Hooks: Write at least {3 - hook_count} more hook option(s)")
        if red_flags:
            print(f"  → Placeholders: Fill in {len(red_flags)} incomplete section(s)")

    print()
    return overall


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DRM Squad: RMBC Brief Validator (Stefan Georgi)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to RMBC brief file (.md or .txt)")
    group.add_argument("--text", type=str, help="Raw brief text to analyze")

    args = parser.parse_args()

    if args.text:
        score = print_rmbc_report(args.text, "inline text")
    else:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File not found: {args.file}")
            sys.exit(2)
        text = file_path.read_text(encoding="utf-8")
        score = print_rmbc_report(text, file_path.name)

    sys.exit(0 if score >= 80 else 1)


if __name__ == "__main__":
    main()
