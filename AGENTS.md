# AGENTS.md

Project-wide instructions for AI agents working in this repository.

## Project

A Persian-first (RTL), bilingual (Persian/English), responsive website for a LEGO center where children build LEGO sets, launched in Iran. Phase 1 delivers the content and marketing MVP; Phases 2–4 (آلبوم, Booking, Payment) are post-MVP. Pages are designed in Figma first, then implemented with Cursor.

Current state, stack, and repository structure: [docs/development-plan.md](docs/development-plan.md) §4 and §10.

## Start here

1. Read [docs/development-plan.md](docs/development-plan.md): roadmap, terminology, documentation map.
2. Read the relevant phase document in `docs/phases/` and the sources it links.

Sources of truth:
- Requirements: `docs/project/project-overview.md`, `docs/project/pages.md`
- Decisions: `docs/project/decisions.md`
- Iran constraints: `docs/project/iran-constraints.md`
- Work breakdown and progress: `docs/phases/phase-*.md`

## Terminology and IDs

Project → MVP → Phase → Stage → Feature → Task → Subtask. These terms are canonical and never interchangeable.

- Phase 1 delivers the MVP. Phases 2–4 are not part of the MVP unless explicitly decided.
- IDs: `PAGE-###`, `S1.3`, `F1.3.2`, `T1.3.2.1`, `DEC-###`, `A-#`. Never renumber or reuse an ID; the next free PAGE-ID is in development-plan §3.2. Subtasks are checklist items under their task.

## Decisions and scope

- Do not invent requirements, features, files, or completed work.
- Do not finalize a `Pending` decision yourself. If work depends on one, ask the user or record the question in `decisions.md`.
- Post-MVP work does not enter Phase 1 without an explicit decision.

## Building for Iran

- No runtime dependency on foreign-hosted resources (fonts, CDNs, scripts, embeds, captchas, maps, analytics) unless approved in `decisions.md`.
- Persian (`fa`, RTL) is the default locale. Use logical CSS properties (start/end), not left/right.

## Documentation

Documentation is updated as part of every change. The workflow, and when to delegate to the `documentation` subagent, is in `.cursor/rules/documentation.mdc`.

Keep each document in the language it is written in; do not translate Persian page names or terms.
