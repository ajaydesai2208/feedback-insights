# Feedback Insights Harness

This folder documents the project-local agent workflow for Feedback Insights.

It is the committed Codex-native equivalent of a requested Claude-style coding harness. The goal is to make planning, bounded specialist work, verification, and fan-in review visible inside the repo without committing global runtime files.

## Why This Exists

The take-home reviewers care about the working app and the agentic coding process. `harness/` keeps that process readable and versioned:

- `agents/`: role cards for bounded specialist agents
- `commands/`: reusable Codex prompts for each project phase
- `skills/`: project-specific workflow playbooks
- `runs/`: temporary or committed specialist reports from parallel branches

## Why Global Runtime Files Are Not Committed

This repo should not contain `.codex`, `.claude`, machine-local hooks, API keys, or global editor config. Those files belong to a user's local environment, not the take-home project.

The committed harness shows how work is coordinated while keeping runtime configuration out of the repo.

## Swarm Workflow

Use one Orchestrator and bounded specialist agents:

- Backend Builder owns `backend/`.
- Frontend Builder owns `frontend/`.
- Eval Agent owns `backend/evals/` during parallel eval work.
- Review Agent performs fan-in verification after specialist work is merged.

Parallelism is allowed only when owned paths are clear and non-overlapping.

## Owned and Forbidden Paths

Owned paths prevent collisions. Forbidden paths prevent specialists from editing shared planning files or another agent's implementation area during fan-out.

During parallel work, specialists write progress to:

```text
harness/runs/<agent>-report.md
```

They should not edit shared files like `PROGRESS.md`, `LOGS.md`, `PLAN.md`, or `TODO.md`. The Orchestrator updates those during fan-in.

## Fan-Out and Fan-In

Fan-out:

1. Orchestrator defines the slice.
2. Each specialist gets owned paths, forbidden paths, and done criteria.
3. Specialists work independently and write reports under `harness/runs/`.

Fan-in:

1. Orchestrator reads specialist reports.
2. Orchestrator resolves integration issues.
3. Review Agent checks correctness and missing verification.
4. Orchestrator updates root docs and remaining tasks.

## Verification Loop

Verification is explicit and project-local:

- backend tests: `python -m pytest backend/tests`
- frontend build: `npm run build --prefix frontend`
- eval harness: `python backend/evals/run_eval.py`
- browser dry run for the full local flow

The eval agent owns the extraction eval harness and reports prompt/schema findings through `harness/runs/` before fan-in.

## Hooks

I did not add a hook layer because this Codex workflow got more value from explicit commands, owned paths, and verification checkpoints. For this scope, hooks would have added ceremony without much signal.
