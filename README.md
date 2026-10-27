# K&A LEGO Center Website

A Persian-first (RTL), bilingual (Persian/English), responsive website for a LEGO center where children build LEGO sets, launched in Iran.

> The official brand name is not decided yet (DEC-012), so this README uses the repository name.

## Status

**Planning.** Phase 1 (MVP), Stage S1.1. There is no application code, technology stack, design, hosting, or domain yet. The repository currently holds documentation, agent configuration, and a documentation link check.

Pages are designed in Figma first, then implemented with Cursor. Current state: [development plan §4](docs/development-plan.md).

## Roadmap

| Phase | Scope | Status |
|---|---|---|
| 1. MVP | Content and marketing website: 13 pages, Persian and English, SEO, analytics, map, CI/CD and automated tests | Planning |
| 2. آلبوم | A separate PWA album of the center's LEGO sets and their availability, integrated into one page | Not scheduled |
| 3. Booking | Reservations for events, workshops, and set construction | Not scheduled |
| 4. Payment | Online payments for bookings and sales | Not scheduled |

Everything above is planned. Nothing is implemented. Details: [development plan](docs/development-plan.md) and the [phase documents](docs/phases/).

## Repository structure

```text
.
├── AGENTS.md                      Instructions for AI agents
├── README.md
├── .cursor/
│   ├── agents/documentation.md    Documentation subagent
│   └── rules/documentation.mdc    Documentation sync rule
├── .github/
│   ├── dependabot.yml             Monthly updates of GitHub Actions
│   └── workflows/ci.yml           CI: documentation link check
├── docs/                          Project documentation (see docs/README.md)
└── scripts/
    └── check-doc-links.py         Checks relative links and anchors in Markdown files
```

The application structure will be documented in [development plan §10](docs/development-plan.md) once the stack is decided.

## Prerequisites

Only the documentation check can run today:

- Git
- Python 3.9 or later (the script uses only the standard library; nothing to install)

Application prerequisites (runtime, package manager) are not defined because the stack is not decided (DEC-016).

## Commands

| Command | Purpose |
|---|---|
| `python scripts/check-doc-links.py` | Verify that every relative link and heading anchor in `.md` and `.mdc` files resolves. Exits with 1 on any broken link |

There are no development, build, lint, or test commands, because there is no application code and no `package.json` or other manifest.

## Configuration

No environment variables or configuration files are needed, and there is no `.env.example`. If the stack requires configuration, an example file will be added without real values.

## Testing

No automated tests exist yet. The testing approach is documented as drafts awaiting approval:

- [Testing strategy](docs/testing/testing-strategy.md): test types, tools, quality gates, and coverage targets
- [Master test plan](docs/testing/test-plan.md): scope, risk-based test matrix, test cycles, and release readiness

## Continuous integration

GitHub Actions workflow [`CI`](.github/workflows/ci.yml) runs the documentation link check on pull requests to `main`, pushes to `main`, and manual runs. Lint, type-check, tests, and build will be added when code exists (T1.3.4.1). A CI guide is not written yet. Branch protection on `main` is a repository setting; whether it is enabled is not recorded in this repository.

## Documentation

Index: [docs/README.md](docs/README.md). Main documents:

- [Development plan](docs/development-plan.md): roadmap, terminology, current state
- [Project overview](docs/project/project-overview.md) and [pages](docs/project/pages.md): requirements
- [Decision register](docs/project/decisions.md): pending and decided decisions
- [Iran constraints](docs/project/iran-constraints.md): connectivity, hosting, services, and legal context

## Development workflow

- Read the [development plan](docs/development-plan.md) and the relevant phase document before starting. [AGENTS.md](AGENTS.md) summarizes the rules for AI agents and the terminology (Phase → Stage → Feature → Task → Subtask, with PAGE, DEC, and other IDs).
- Do not invent requirements. Do not decide a `Pending` decision yourself; record or ask.
- Post-MVP work does not enter Phase 1 without an explicit decision.
- Update documentation in the same change as the work ([workflow](.cursor/rules/documentation.mdc)), and run `python scripts/check-doc-links.py`.
- Contribution guidelines, a branching policy, and a pull request template are not defined yet.

## Building for Iran

- No runtime dependency on foreign-hosted resources (fonts, CDNs, scripts, embeds, captchas, maps, analytics) unless approved in the decision register.
- Persian (`fa`, RTL) is the default locale; use logical CSS properties (start/end), not left/right.
- Details: [Iran constraints](docs/project/iran-constraints.md).

## Security

- Never commit secrets, credentials, tokens, or personal data. CI currently needs no secrets.
- Do not publish photos or videos of children without a consent policy (DEC-013, pending).
- No security policy or vulnerability reporting process exists yet. Until one is defined, report security concerns to the project owner directly.

## License

No license has been established yet, so no `LICENSE` file exists.
