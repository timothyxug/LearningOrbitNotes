# OrbitIdeaForge

OrbitIdeaForge is a solo learning project that captures the real-world feel of tinkering with ideas after work hours. It generates randomized concept prompts for future side projects covering tools, finance, AI, bots, scripts, and learning utilities, with equal weight for web2 and web3 possibilities.

## Goals
- reproduce the messy, exploratory backlog of a single developer building a learning portfolio
- surface concise prompts that can seed short experiments or blog exercises
- document the evolution of the project with real-sounding commit notes and logs

## Structure
- `src/`: core generator logic, utilities, and CLI entry point
- `data/`: curated idea fragments and narrative seeds for the generator
- `docs/`: notes, experiment logs, and roadmap sketches that mirror personal journal entries

## Running the idea generator
The CLI runner at `src/runner.ts` prints one curated idea with a description and three practice steps. Use `ts-node src/runner.ts` or adapt the script for Deno or a lightweight build as the project evolves.

## Daily practice notes
- Refresh `docs/lab-notes.md` after every evening session so the audit trail stays vivid.
- Append new rows to `docs/experiment-log.md` when a prompt feels worth chasing; this log doubles as my weekly review.
- Keep `docs/roadmap.md` aligned with the next handful of tickets so the repo behaves like an actual side project backlog.
