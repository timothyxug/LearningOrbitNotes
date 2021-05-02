"""Create a lightweight report for a Learning Orbit session."""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from textwrap import indent

from src.learning_orbit import create_session, timeline_hint


def serialize_entry(entry):
    return {
        "topic": entry.topic,
        "focus": entry.focus,
        "style": entry.style,
        "duration_minutes": entry.duration_minutes,
        "resources": entry.resources,
        "mood": entry.mood,
        "tactics": entry.tactics,
    }


def build_report(session, compact: bool = False):
    report = {
        "plan": asdict(session.prompt),
        "entries": [serialize_entry(e) for e in session.entries],
        "timeline": timeline_hint(session.entries),
    }
    if compact:
        return json.dumps(report, ensure_ascii=False)
    return json.dumps(report, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dump a Learning Orbit session report.")
    parser.add_argument("-n", "--entries", type=int, default=5, help="Number of entries")
    parser.add_argument("-s", "--seed", type=int, help="Seed for repeatable sessions")
    parser.add_argument("-o", "--output", help="Optional file path for the report")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")

    args = parser.parse_args()
    session = create_session(args.entries, seed=args.seed)
    payload = build_report(session, compact=args.compact)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(payload)
        print(f"Report written to {args.output}")
    else:
        print("Session report")
        print(indent(payload, "  "))


if __name__ == "__main__":
    main()
