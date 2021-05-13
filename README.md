# Learning Orbit Notes

A solo effort named **Learning Orbit Capsule** that keeps sketchy, high-level reflections on orbital science, software craftsmanship, and other study tracks. Each edit here leans on the rhythm of a side project: a short sprint, a quiet pause, and a quick log update so the momentum feels real.

## Project Goals
- generate structured notes and learning outlines on random prompts so the log always has something new to tweak.
- pretend to follow the rhythm of a one-person side project (slow progress, short bursts of work, plenty of small milestones).
- stay easy to run locally with minimal dependencies and a simple CLI.
- keep the project narrative obvious: each change is a small research note or helper utility that could sit on a personal repo for other side goals.

## Structure
- `src/learning_orbit.py` exposes the generator primitives.
- `README` documents the habit and usage, giving the feel of an ongoing journal-like project.
- `scripts/compose_notes.py` is the entry point to build and inspect a new batch of ideas.

## Side Project Rhythm
- Note entries are sketched, then lightly shaped into a timeline so the whole repo reads like the notebook of a determined hobbyist.
- New helpers (scripts, modules, tests) are added one at a time, just enough to keep the stub project alive without overhauling everything at once.

## Usage
1. Update `src/learning_orbit.py` when a new topic or learning style pops into the notebook.
2. Run `python scripts/compose_notes.py` to see an ensemble of study fragments for the day.
3. Save the output somewhere meaningful (not in this repo) to keep the energy stored offline.

## Session Reports
- `python scripts/compose_notes.py --plan` prints the session prompt before the entries so the intention is always visible.
- `python scripts/session_report.py` dumps the same prompt plus entry details and timeline as JSON for later journaling; use `--output` to capture it and `--compact` when the file should stay terse.

## Future Work
- capture the generated notes into a simple JSON timeline for manual review.
- stitch the habits into a cheap automation so each run records a timestamp and mood.
- eventually draft a little blog post describing the entire fake project timeline.
