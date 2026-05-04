# Logs

Simple debugging and change log for commands, failures, fixes, and decisions.

## Format

```text
### YYYY-MM-DD: Short Title

Context:
- What was being changed or verified.

Commands:
- Exact commands run, if any.

Result:
- Pass, fail, skipped, or blocked.

Decision:
- Any important implementation or workflow decision.

Follow-up:
- Remaining work or owner.
```

## Entries

### 2026-05-04: Initial Structure

Context:
- Created the Feedback Insights project scaffold.

Commands:
- No dependency installation commands were run.

Result:
- Project-local docs, backend placeholders, frontend placeholders, eval placeholders, and harness docs exist.

Decision:
- Use `harness/` as the committed project-local agent workflow instead of global runtime config.

Follow-up:
- Complete Phase 1 documentation refinement, then start the backend vertical slice.
