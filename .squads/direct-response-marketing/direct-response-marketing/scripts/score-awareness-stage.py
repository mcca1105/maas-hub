#!/usr/bin/env python3
"""
DRM Squad: Awareness Stage Scorer
Analyzes copy or market research data to determine which Eugene Schwartz
awareness stage (1-5) the copy is optimized for, and whether it matches
the target audience's actual stage.

Usage:
    python score-awareness-stage.py --copy path/to/copy.md
    python score-awareness-stage.py --research path/to/voc-data.md
    python score-awareness-stage.py --both --copy copy.md --research voc.md
    python score-awareness-stage.py --text "Paste copy or research text here"

Eugene Schwartz Awareness Stages:
    Stage 1: Unaware — doesn't know they have the problem
    Stage 2: Problem Aware — knows the problem, not the solution
    Stage 3: Solution Aware — knows solutions exist, not your product
    Stage 4: Product Aware — knows your product, not fully committed
    Stage 5: Most Aware — knows your product and price, just needs the deal
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
# STAGE SIGNAL PATTERNS
# ─────────────────────────────────────────────────────────────────────────────

STAGE_SIGNALS = {
    1: {
        "name": "Unaware",
        "description": "Prospect doesn't know they have the problem yet",
        "copy_strategy": "Lead with a pattern interrupt or shocking revelation about a hidden problem",
        "headline_patterns": [
            r'\bwarning\b', r'\bdanger\b', r'\bhidden\b', r'\bsecret\b',
            r'\bsurprising\b', r'\bshocking\b', r'\bunknown\b',
            r'\bmost .+ don\'t know\b', r'\bwhat you don\'t know\b',
        ],
        "content_signals": [
            r'\byou may not realize\b', r'\bwithout knowing\b',
            r'\bwhat many .+ don\'t\b', r'\bsurprising truth\b',
            r'\bthe hidden\b', r'\bundiscovered\b',
        ],
    },
    2: {
        "name": "Problem Aware",
        "description": "Knows the problem, frustrated, looking for answers",
        "copy_strategy": "Validate their problem, name it precisely, position solution as new approach",
        "headline_patterns": [
            r'\bare you .+ (struggling|tired|frustrated|sick)\b',
            r'\bdo you .+ (want|need|wish|hate|dread)\b',
            r'\bif you\'re .+ (stuck|frustrated|struggling)\b',
            r'\bwhy .+ (doesn\'t|can\'t|won\'t)\b',
        ],
        "content_signals": [
            r'\bfrustrat\w+\b', r'\bstruggl\w+\b', r'\btired of\b',
            r'\bsick of\b', r'\bfed up\b', r'\bno matter what\b',
            r'\bnothing works\b', r'\bI\'ve tried\b', r'\byou\'ve tried\b',
        ],
    },
    3: {
        "name": "Solution Aware",
        "description": "Knows solutions exist, shopping for the right one",
        "copy_strategy": "Introduce your unique mechanism as a new/better solution category",
        "headline_patterns": [
            r'\ba new (way|method|approach|system)\b',
            r'\bfinally\b.*\bway\b',
            r'\bdiscov\w+\b.*\bmethod\b',
            r'\bbreakthrough\b',
            r'\bunlike .+ else\b',
        ],
        "content_signals": [
            r'\bunlike (other|traditional|conventional)\b',
            r'\bnew approach\b', r'\bnew method\b', r'\bnew way\b',
            r'\bdifferent (from|than)\b', r'\binstead of\b',
            r'\bwhat makes .+ different\b', r'\bwhy .+ works\b',
        ],
    },
    4: {
        "name": "Product Aware",
        "description": "Knows the product, not yet convinced to buy",
        "copy_strategy": "Overcome specific objections, reinforce benefits, sharpen the offer",
        "headline_patterns": [
            r'\bwhy .+ (is|are) different\b',
            r'\bhow .+ (works|helped)\b',
            r'\bwhat .+ (users|customers|members) (say|report)\b',
            r'\bcompared to\b',
        ],
        "content_signals": [
            r'\bstill (thinking|considering|unsure)\b',
            r'\byou may be wondering\b', r'\blet me explain\b',
            r'\bhere\'s what .+ (get|include|receive)\b',
            r'\btestimonial\b', r'\bcustomer\b', r'\breviews?\b',
            r'\bcompetitor\b', r'\bcompared\b', r'\bversus\b',
        ],
    },
    5: {
        "name": "Most Aware",
        "description": "Ready to buy, just needs the right offer/price",
        "copy_strategy": "Lead with offer, price, bonus, deadline — make it easy to say yes",
        "headline_patterns": [
            r'\b\d+% off\b', r'\bsave \$\d+\b',
            r'\btoday only\b', r'\blimited time\b',
            r'\bspecial (offer|price|deal)\b',
            r'\bget .+ (now|today|instantly)\b',
            r'\bfinal (sale|chance|call)\b',
        ],
        "content_signals": [
            r'\border now\b', r'\bbuy now\b', r'\bcheck out\b',
            r'\badd to cart\b', r'\bprice\b.*\$\d+',
            r'\bcoupon\b', r'\bdiscount\b', r'\bpromo\b',
            r'\bexpires?\b', r'\bdeadline\b', r'\bends\b.*\b(today|tonight|soon)\b',
        ],
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# VOC SIGNALS (what research text reveals about the audience)
# ─────────────────────────────────────────────────────────────────────────────

VOC_AWARENESS_SIGNALS = {
    1: {
        "indicators": [
            r'\bI didn\'t know\b', r'\bnever realized\b', r'\bhad no idea\b',
            r'\bnever thought\b', r'\bdidn\'t think .+ was\b',
        ],
    },
    2: {
        "indicators": [
            r'\bI\'ve tried everything\b', r'\bnothing works\b',
            r'\bwhy (can\'t|don\'t|won\'t) I\b',
            r'\bso frustrated\b', r'\bso tired\b', r'\bI just want\b',
            r'\bI wish\b', r'\bI hate\b',
        ],
    },
    3: {
        "indicators": [
            r'\bI\'ve tried .+but\b', r'\bI looked at\b',
            r'\bI found .+(doesn\'t|didn\'t)\b',
            r'\bI need something (different|better|that actually)\b',
            r'\bI\'m looking for\b',
        ],
    },
    4: {
        "indicators": [
            r'\bI\'ve heard of\b', r'\bI saw\b', r'\bI know about\b',
            r'\bbut (I\'m not sure|I don\'t know if)\b',
            r'\bis it (really|actually|worth it)\b',
            r'\bI want to (know|understand|see) (more|if|how)\b',
        ],
    },
    5: {
        "indicators": [
            r'\bwhere can I\b', r'\bhow do I (buy|get|order|sign up)\b',
            r'\bwhat\'s the price\b', r'\bhow much\b.*\bcost\b',
            r'\bdo you have a discount\b', r'\bis there a coupon\b',
        ],
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# SCORING
# ─────────────────────────────────────────────────────────────────────────────

def score_text_for_stage(text: str, signal_dict: dict) -> dict:
    """Score a text against all 5 awareness stage signal sets."""
    text_lower = text.lower()
    stage_scores = {}

    for stage_num, signals in signal_dict.items():
        score = 0
        matched_signals = []

        all_patterns = signals.get("headline_patterns", []) + signals.get("content_signals", []) + signals.get("indicators", [])

        for pattern in all_patterns:
            matches = re.findall(pattern, text_lower)
            if matches:
                score += len(matches)
                matched_signals.extend(matches[:2])

        stage_scores[stage_num] = {
            "score": score,
            "matched_signals": list(set(matched_signals))[:5],
        }

    # Normalize scores
    max_score = max((s["score"] for s in stage_scores.values()), default=1) or 1
    for stage_num in stage_scores:
        stage_scores[stage_num]["normalized"] = stage_scores[stage_num]["score"] / max_score

    # Determine dominant stage
    dominant = max(stage_scores, key=lambda s: stage_scores[s]["score"])

    return {
        "stage_scores": stage_scores,
        "dominant_stage": dominant,
        "dominant_name": STAGE_SIGNALS[dominant]["name"],
        "confidence": "HIGH" if stage_scores[dominant]["score"] >= 5 else "MEDIUM" if stage_scores[dominant]["score"] >= 2 else "LOW",
    }


def analyze_copy(text: str) -> dict:
    """Analyze copy text for awareness stage calibration."""
    return score_text_for_stage(text, STAGE_SIGNALS)


def analyze_voc(text: str) -> dict:
    """Analyze VOC/research text to determine audience's actual stage."""
    return score_text_for_stage(text, VOC_AWARENESS_SIGNALS)


# ─────────────────────────────────────────────────────────────────────────────
# REPORTING
# ─────────────────────────────────────────────────────────────────────────────

def print_stage_scores(scores: dict, label: str):
    """Print a visual stage score breakdown."""
    stage_scores = scores["stage_scores"]

    print(f"\n{label}")
    print(f"  Dominant Stage: {scores['dominant_stage']} ({scores['dominant_name']}) — {scores['confidence']} confidence")
    print()
    for stage_num in range(1, 6):
        data = stage_scores.get(stage_num, {"score": 0, "normalized": 0, "matched_signals": []})
        stage_name = STAGE_SIGNALS[stage_num]["name"]
        bar_length = int(data["normalized"] * 20)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        marker = " ◄" if stage_num == scores["dominant_stage"] else ""
        print(f"  Stage {stage_num} ({stage_name:15}): [{bar}] {data['score']:3} signals{marker}")
        if data.get("matched_signals"):
            print(f"    Matches: {', '.join(str(m) for m in data['matched_signals'][:3])}")
    print()


def print_match_analysis(copy_result: dict, voc_result: dict):
    """Compare copy calibration vs. audience stage and print recommendations."""
    copy_stage = copy_result["dominant_stage"]
    audience_stage = voc_result["dominant_stage"]

    print(f"{'='*60}")
    print("MATCH ANALYSIS")
    print(f"{'='*60}")
    print(f"  Copy calibrated for:  Stage {copy_stage} ({STAGE_SIGNALS[copy_stage]['name']})")
    print(f"  Audience actually at: Stage {audience_stage} ({STAGE_SIGNALS[audience_stage]['name']})")
    print()

    if copy_stage == audience_stage:
        print("  ✅ MATCH: Copy is calibrated for the correct awareness stage")
    elif copy_stage < audience_stage:
        gap = audience_stage - copy_stage
        print(f"  ❌ MISMATCH: Copy is {gap} stage(s) BELOW audience level")
        print(f"  Problem: Copy talks to people at Stage {copy_stage}, but audience is at Stage {audience_stage}")
        print(f"  Risk: Copy feels elementary or condescending to this audience")
        print(f"  Fix: Move copy up to Stage {audience_stage} strategy:")
        print(f"  → {STAGE_SIGNALS[audience_stage]['copy_strategy']}")
    else:
        gap = copy_stage - audience_stage
        print(f"  ❌ MISMATCH: Copy is {gap} stage(s) ABOVE audience level")
        print(f"  Problem: Copy assumes awareness the audience doesn't have")
        print(f"  Risk: Copy will confuse or fail to engage cold audience")
        print(f"  Fix: Move copy down to Stage {audience_stage} strategy:")
        print(f"  → {STAGE_SIGNALS[audience_stage]['copy_strategy']}")
    print()


def print_recommendations(dominant_stage: int):
    """Print copy strategy recommendations for the target stage."""
    stage_info = STAGE_SIGNALS[dominant_stage]
    print(f"{'='*60}")
    print(f"COPY STRATEGY FOR STAGE {dominant_stage} ({stage_info['name'].upper()})")
    print(f"{'='*60}")
    print(f"  Description: {stage_info['description']}")
    print(f"  Strategy: {stage_info['copy_strategy']}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DRM Squad: Eugene Schwartz Awareness Stage Scorer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--copy", type=str, help="Path to copy file")
    parser.add_argument("--research", type=str, help="Path to VOC/market research file")
    parser.add_argument("--text", type=str, help="Direct text input")
    parser.add_argument("--mode", choices=["copy", "research", "both"], default="copy",
                        help="What to analyze: copy calibration, research to find audience stage, or both")

    args = parser.parse_args()

    print(f"\n{'='*60}")
    print("DRM SQUAD: AWARENESS STAGE SCORER")
    print(f"{'='*60}")

    copy_result = None
    voc_result = None

    # Handle copy analysis
    if args.text:
        print("\n[Analyzing direct text input as COPY]")
        copy_result = analyze_copy(args.text)
        print_stage_scores(copy_result, "COPY AWARENESS CALIBRATION:")
        print_recommendations(copy_result["dominant_stage"])

    elif args.copy or args.mode in ("copy", "both"):
        if args.copy:
            path = Path(args.copy)
            if not path.exists():
                print(f"Error: Copy file not found: {args.copy}")
                sys.exit(2)
            text = path.read_text(encoding="utf-8")
            print(f"\nAnalyzing copy: {path.name}")
            copy_result = analyze_copy(text)
            print_stage_scores(copy_result, "COPY AWARENESS CALIBRATION:")

    # Handle research/VOC analysis
    if args.research or args.mode == "research":
        if args.research:
            path = Path(args.research)
            if not path.exists():
                print(f"Error: Research file not found: {args.research}")
                sys.exit(2)
            text = path.read_text(encoding="utf-8")
            print(f"\nAnalyzing VOC research: {path.name}")
            voc_result = analyze_voc(text)
            print_stage_scores(voc_result, "AUDIENCE AWARENESS STAGE (from VOC research):")

    # Match analysis (when both available)
    if copy_result and voc_result:
        print_match_analysis(copy_result, voc_result)
        # Recommend based on audience, not copy
        print_recommendations(voc_result["dominant_stage"])

    elif copy_result:
        print_recommendations(copy_result["dominant_stage"])

    elif voc_result:
        print_recommendations(voc_result["dominant_stage"])
    else:
        print("No analysis performed. Use --copy, --research, or --text to provide input.")
        sys.exit(2)


if __name__ == "__main__":
    main()
