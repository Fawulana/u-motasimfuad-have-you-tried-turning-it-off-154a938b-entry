#!/usr/bin/env python3
"""Entry for "Have You Tried Turning It Off?" (make.fun).

Writes one funny line — a hopeless tech support agent's reply to a
desperate customer — to /output/entry.txt.

Deterministic, offline, standard library only: the line is a constant,
so every run writes the exact same bytes.
"""

import os

# The line: cheerful escalation to "Level 2 support" — which turns out to
# be the same agent in a different headset. The humour is the agent's
# cheerful uselessness; the customer is never the butt of it. At 117
# characters it sits comfortably inside the gate's 1–199 character band,
# and the good-news/bad-news frame sells the agent's cheerfulness before
# the twist lands.
LINE = (
    "Good news \u2014 I've escalated your case to Level 2 support. "
    "Bad news \u2014 that's also me, just wearing a different headset."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
