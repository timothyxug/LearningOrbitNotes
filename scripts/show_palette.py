"""Inspect a fresh palette for the next Learning Orbit session."""
from __future__ import annotations

import argparse

from src.topic_palette import session_prompt


def main() -> None:
    parser = argparse.ArgumentParser(description="Peek at the palette of session hints.")
    parser.add_argument("-s", "--seed", type=int, help="Seed to reproduce a palette")
    args = parser.parse_args()

    prompt = session_prompt(seed=args.seed)
    print("Palette peek")
    print(f"Mood: {prompt.mood}")
    print(f"Topics: {', '.join(prompt.topics)}")
    print(f"Approach: {prompt.approaches[0] if prompt.approaches else ''}")
    print(f"Tactics: {', '.join(prompt.tactics)}")


if __name__ == "__main__":
    main()
