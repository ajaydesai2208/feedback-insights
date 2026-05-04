# Agent Swarm Coordination

Project-specific playbook for bounded parallel Codex work.

## Use When

Use this only when two or more tasks can proceed without touching the same paths, such as backend implementation and eval data preparation.

Do not use a swarm for a small single-file change.

## Fan-Out Checklist

- Define the goal and current phase.
- Assign each agent a role card from `harness/agents/`.
- Name owned paths and forbidden paths.
- Name the report file under `harness/runs/`.
- Name done criteria and verification commands.
- Confirm shared root docs are Orchestrator-only during fan-out.

## Fan-In Checklist

- Read all specialist reports.
- Compare API and type contracts.
- Resolve integration conflicts in one place.
- Run relevant verification commands.
- Update `PROGRESS.md`, `LOGS.md`, and `TODO.md`.
- Ask Review Agent for final findings after integration.

## Collision Rules

- No two agents edit the same path in parallel.
- Specialists do not edit shared root docs during fan-out.
- Eval Agent may recommend prompt or schema edits, but does not take them without ownership.
- Review Agent is read-only unless assigned a narrow fix.

## Report Template

```text
# <Agent> Report

Scope:
Owned paths:
Files changed:
Verification:
Known issues:
Requests for Orchestrator:
```
