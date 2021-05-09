"""Basic sanity checks for the Learning Orbit modules."""
from __future__ import annotations

from src.learning_orbit import create_session, timeline_hint


def test_session_entries_share_prompt_mood() -> None:
    session = create_session(size=3, seed=9)
    assert len(session.entries) == 3
    assert all(entry.mood == session.prompt.mood for entry in session.entries)


def test_timeline_matches_entry_count() -> None:
    session = create_session(size=4, seed=17)
    timeline = timeline_hint(session.entries)
    assert len(timeline) == len(session.entries)
    assert all("+" in line for line in timeline)
