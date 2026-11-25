#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Scores several original smart-fridge roast lines against the house
judge's five criteria (most important first) and writes the winning
line to /output/entry.txt.

Judge criteria and weights:
  1. On-subject roast of a smart fridge (gate)      weight 5
  2. Punchline lands on first read                  weight 4
  3. Specific to smart fridges, not any gadget      weight 3
  4. Tight wording, every word earns its place     weight 2
  5. Fresh angle, dodges the obvious cracks        weight 1
"""

import os

# (line, on_subject, punchline, specificity, tightness, freshness)
# Each criterion scored 0-10 by hand against the judge brief.
CANDIDATES = [
    (
        "My fridge's ice maker takes twenty minutes to make three cubes, "
        "then beeps like it just landed a rover on Mars.",
        10, 7, 9, 7, 7,
    ),
    (
        "My fridge has a camera inside and still lets the milk expire - "
        "it watches everything and judges nothing.",
        10, 7, 8, 8, 6,
    ),
    (
        "My fridge texted me at 3 a.m. to say the door was open. It was. "
        "I was standing in front of it, eating.",
        10, 10, 9, 9, 9,
    ),
    (
        "My fridge's touchscreen shows ads now - I paid two grand for an "
        "appliance that sells me yogurt while I'm buying yogurt.",
        10, 8, 9, 7, 8,
    ),
    (
        "I asked my fridge for a snack idea. It suggested I close the "
        "door and reflect on my choices.",
        10, 8, 7, 9, 8,
    ),
    (
        "My fridge sends me a weekly energy report like a passive-"
        "aggressive landlord, then leaves its own light on all night.",
        10, 7, 8, 7, 7,
    ),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate):
    line, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def main():
    # Gate first: drop any candidate the scorer would refuse outright.
    valid = [c for c in CANDIDATES if 1 <= len(c[0]) <= 200 and c[0].strip()]
    assert valid, "no candidate passes the 1-200 char gate"
    # Highest total wins; ties break to the shorter line (tighter wording).
    ranked = sorted(valid, key=lambda c: (score(c), -len(c[0])), reverse=True)
    print("candidate scores (gate/punch/specific/tight/fresh -> total):")
    for line, *marks in ranked:
        print(f"  {score((line, *marks)):3d}  {line}")
    winner = ranked[0][0]
    assert 1 <= len(winner) <= 200, "winning line must be 1-200 chars"
    assert winner.strip(), "winning line must not be only whitespace"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(winner)
    except OSError:
        path = "entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(winner)
    print(f"\nwinner ({len(winner)} chars) -> {path}")
    print(winner)


if __name__ == "__main__":
    main()
