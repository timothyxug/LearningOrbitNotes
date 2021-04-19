"""Core note generator primitives for Learning Orbit Notes."""
from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import timedelta
from typing import Iterable, List

from src.topic_palette import SessionPrompt, session_prompt

TOPIC_FRAGMENTS = [
    "orbital mechanics",
    "decentralized notebooks",
    "edge AI on satellites",
    "human-in-the-loop automations",
    "signal processing cheatsheets",
    "personal workflow rituals",
    "spatial data sketches",
    "simulated trajectory logs",
]

RESOURCE_HINTS = [
    "sketch the flow by hand before coding",
    "pull open-source examples from an old repo",
    "write a quick explainer for a mentor",
    "build a 10-line diagram rather than read another paper",
    "pretend you are teaching a crash course",
    "record the idea in a short voice memo",
]

STUDY_STYLES = [
    "short journal entry",
    "tabular comparison",
    "three-minute demo",
    "private Twitter thread",
    "whiteboard snapshot",
    "audio note",
]


@dataclass
class NoteEntry:
    topic: str
    focus: str
    style: str
    duration_minutes: int
    resources: List[str]
    mood: str
    tactics: List[str]

    def summarize(self) -> str:
        """Return a quick human-readable summary of the entry."""
        resources_line = "; ".join(self.resources)
        tactics_line = ", ".join(self.tactics) if self.tactics else "none"
        return (
            f"{self.topic} — focus: {self.focus} ({self.duration_minutes}m)\n"
            f"Style: {self.style} | Mood: {self.mood} | Tactics: {tactics_line}\n"
            f"Resources: {resources_line}"
        )


@dataclass
class StudySession:
    entries: List[NoteEntry]
    prompt: SessionPrompt

    def describe_plan(self) -> str:
        """Describe the session prompt that informed these entries."""
        topic_list = ", ".join(self.prompt.topics)
        approach = self.prompt.approaches[0] if self.prompt.approaches else ""
        tactic = ", ".join(self.prompt.tactics)
        return (
            f"Plan: topics [{topic_list}] | approach: {approach}\n"
            f"Mood: {self.prompt.mood} | tactic: {tactic}"
        )


def _pick_many(source: Iterable[str], count: int) -> List[str]:
    """Pick up to `count` unique items from `source`."""
    pool = list(source)
    random.shuffle(pool)
    return pool[:count]


def create_entry(
    *,
    topic_hint: str | None = None,
    focus_hint: str | None = None,
    style_hint: str | None = None,
    mood: str = "curious",
    tactics: Iterable[str] | None = None,
) -> NoteEntry:
    """Create a single note entry with balanced random attributes."""
    topic = topic_hint or random.choice(TOPIC_FRAGMENTS)
    focus = focus_hint or random.choice(RESOURCE_HINTS)
    style = style_hint or random.choice(STUDY_STYLES)
    duration = random.choice([15, 20, 25, 30, 45])
    resources = _pick_many(RESOURCE_HINTS, min(2, len(RESOURCE_HINTS)))
    tactic_list = list(tactics) if tactics is not None else []
    return NoteEntry(topic, focus, style, duration, resources, mood, tactic_list)


def create_session(size: int = 5, seed: int | None = None) -> StudySession:
    """Build a StudySession guided by a palette hint."""
    prompt = session_prompt(seed)
    entries: List[NoteEntry] = []
    for index in range(size):
        topic_hint = prompt.topics[index] if index < len(prompt.topics) else None
        entries.append(
            create_entry(
                topic_hint=topic_hint,
                mood=prompt.mood,
                tactics=prompt.tactics,
            )
        )
    return StudySession(entries, prompt)


def build_batch(size: int = 5, seed: int | None = None) -> List[NoteEntry]:
    """Build a batch of entries that resembles a single productive session."""
    session = create_session(size, seed)
    return session.entries


def timeline_hint(batch: List[NoteEntry]) -> List[str]:
    """Produce a loose timeline between entries to mimic slower-paced work."""
    entries: List[str] = []
    current_time = timedelta(hours=0)
    for entry in batch:
        gap = random.choice([15, 20, 30, 45, 60])
        entries.append(
            f"+{current_time} — {entry.topic} ({entry.duration_minutes} min of {entry.style})"
            f" | mood: {entry.mood}"
        )
        current_time += timedelta(minutes=entry.duration_minutes + gap)
    return entries
