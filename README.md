# OrbitIdeaForge

OrbitIdeaForge is a solo learning project that captures the real-world feel of tinkering with ideas after work hours. It generates randomized concept prompts for future side projects covering tools, finance, AI, bots, scripts, and learning utilities, with equal weight for web2 and web3 possibilities.

## Goals
- capture the messy, exploratory backlog of a single developer building a learning portfolio
- produce concise prompts that can seed short experiments or blog exercises
- document the evolution of the project with brief, real-sounding commit notes

## Structure
- `src/`: core generator logic and helper utilities
- `data/`: curated idea fragments and templates to support random prompts
- `docs/`: developer notes, lesson logs, and improvisational roadmaps

## Running the idea generator
There is a CLI entry point under `src/runner.ts` that can be used to produce ideas from the command line or extend the generator for new formats. All code is written in TypeScript so the project can grow (for example) into a Deno script or a quick node-based prototype later.

## Daily practice notes
- Keep `docs/lab-notes.md` fresh after each moderate coding session to capture what really changed and why it felt interesting.
- Dump thoughts into `docs/experiment-log.md` when an idea feels worth revisiting; that log is my nightly review for the week.
- The roadmap file tracks the next three tickets so even this tiny repo feels like a living weekend project.
