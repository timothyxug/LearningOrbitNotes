"""Lightweight CLI to simulate a Learning Orbit Notes session."""
from __future__ import annotations

import argparse
import random
import textwrap

from src.learning_orbit import create_session, timeline_hint


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compose a batch of Learning Orbit Notes."
    )
    parser.add_argument(
        "-n",
        "--entries",
        type=int,
        default=5,
        help="Number of entries to draft in this session.",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        help="Optional seed so that the same session can be replayed.",
    )
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Include the session plan prompt before the entries.",
    )
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    session = create_session(args.entries, seed=args.seed)
    batch = session.entries
    if args.plan:
        print("Session plan")
        print(session.describe_plan())
        print()
    timeline = timeline_hint(batch)

    print("Learning Orbit Notes — Session Preview\n")
    for entry in batch:
        print(entry.summarize())
        print("---")

    print("Timeline sketch:")
    timeline_block = "\n".join(timeline)
    print(textwrap.indent(timeline_block, "  "))


if __name__ == "__main__":
    main()
