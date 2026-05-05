# Final Submission Notes

Feedback Insights is a local React/FastAPI app that extracts sentiment, themes, and explicit action items from pasted customer feedback using the OpenAI API, stores results in SQLite, and shows dashboard summaries. The decisions I am proudest of are about keeping the agent work visible and controlled.

First, I made the workflow project-local. `AGENTS.md` carries the load-bearing context: architecture, API contract, extraction contract, file ownership, verification commands, and no-secret rules. `harness/` is the Codex-native harness for this repo instead of committed global Codex config. It gives the reviewer the actual operating model: role cards, reusable prompts, project playbooks, and fan-in reports.

Second, I used bounded swarm work rather than a loose pile of agents. The Orchestrator owned planning and fan-in. Backend Builder owned `backend/`, Frontend Builder owned `frontend/`, Extraction Eval Agent owned `backend/evals/`, and the Review/Fan-in Agent reconciled the branches. Owned paths and forbidden paths mattered because they prevented parallel edits from colliding. The `harness/runs/*-report.md` files show what each branch did and what fan-in had to resolve.

Third, I chose one stretch goal and made it useful: the extraction eval harness. It uses golden examples, reruns the provider-backed prompt path, validates the same app schema, and writes an aggregate report. During fan-in I changed it to reuse the app prompt and Pydantic schema instead of carrying a separate prompt path, which reduced drift between the demo and the eval.

One thing that did not work cleanly was relying on happy-path integration. Fan-in and browser testing surfaced rough edges: frontend/backend response shape mismatch, overly aggressive batch parsing, and SQLite connection ownership during immediate post-submit refresh. I fixed those by making the backend contract canonical, preserving each non-empty line as one feedback entry, and tightening SQLite connection ownership so route handlers open and close their own connections.

Provider-backed verification was completed from a local shell with secrets kept out of the repo. If this were long-lived, I would add more golden examples, regression gates around the eval harness, and a small preflight command for environment visibility, ignored artifacts, API contract checks, and SQLite behavior. I did not add a hook layer because this Codex workflow got more value from explicit commands, owned paths, and verification checkpoints. For this scope, hooks would have added ceremony without much signal.
