"""Collection of palette items that shape a Learning Orbit session."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, List

TOPIC_PALETTE = [
    "orbital rendezvous notes",
    "attitude control experiments",
    "constellation ops rituals",
    "signal integrity anecdotes",
    "payload software playbooks",
    "ground segment diagrams",
    "satellite choreography scripts",
    "mission pattern sketches",
]

@dataclass
class SessionPrompt:
    topics: List[str]
    approaches: List[str]
    tactics: List[str]
    mood: str


APPROACH_PIVOTS = [
    "map assumptions before coding",
    "rewrite past field notes as diagrams",
    "rebuild a small helper in a new language",
    "record a five-minute recap",
    "mock an interview question around the topic",
    "trace hardware expectations on paper",
]

TACTICS = [
    "break the timeline into sprints",
    "annotate the repo with the day's mood",
    "pin a single reference asset for later",
    "bundle ten ideas into a tiny play",
    "skip the perfect solution and ship a draft",
    "revisit a dead branch for inspiration",
]

MOODS = [
    "curious",
    "detached",
    "focused",
    "pensive",
    "playful",
    "sleepless",
]


def pick_items(source: Iterable[str], count: int) -> List[str]:
    """Sample up to `count` items without replacement."""
    pool = list(source)
    random.shuffle(pool)
    return pool[:count]


def session_prompt(seed: int | None = None) -> SessionPrompt:
    """Return a tight set of hints that guide a single session."""
    if seed is not None:
        random.seed(seed)
    return SessionPrompt(
        topics=pick_items(TOPIC_PALETTE, 2),
        approaches=pick_items(APPROACH_PIVOTS, 1),
        tactics=pick_items(TACTICS, 1),
        mood=random.choice(MOODS),
    )
