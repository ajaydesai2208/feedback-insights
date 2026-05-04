# Final Submission Notes

Feedback Insights is a local React/FastAPI app that extracts sentiment, themes, and explicit action items from pasted customer feedback using the OpenAI API, stores results in SQLite, and shows dashboard summaries. The work I am proudest of is mostly context engineering, not just code generation.

First, I made the agent workflow project-local and reviewable. `AGENTS.md` defines the architecture, API contract, OpenAI extraction contract, file ownership, verification commands, and no-secret rules. `harness/` is the Codex-native equivalent of an agentic coding harness: role cards, reusable commands, project skills, and fan-in reports live in the repo instead of hidden global config.

Second, I used bounded parallelism deliberately. The Orchestrator owned planning and fan-in. Backend Builder owned `backend/`, Frontend Builder owned `frontend/`, Extraction Eval Agent owned `backend/evals/`, and the Review/Fan-in Agent reconciled the branches. Each role had owned paths and forbidden paths so parallel agents would not edit the same files or shared docs at the same time. The `harness/runs/*-report.md` files are the evidence trail used during fan-in.

Third, I treated the eval harness as the meaningful stretch goal. It is not a large testing framework; it is a small golden-data loop that checks the same extraction behavior the app uses. During fan-in, I changed the eval runner to reuse the app prompt and Pydantic schema instead of carrying a separate prompt path. That reduced drift between demo behavior and eval behavior.

One thing that did not work cleanly was frontend/backend contract alignment. The frontend initially expected slightly different field names and a different sentiment distribution shape than the backend returned. Fan-in surfaced this quickly, and I fixed it by making the backend response shape canonical and updating frontend types/components to match. A second issue was provider verification from Codex: the command process could not see `OPENAI_API_KEY`, so provider-backed verification was completed manually from a local PowerShell process with secrets kept out of the repo.

If this were a long-lived project, I would add a small preflight harness command that validates environment visibility, dependency state, ignored artifacts, and API contract compatibility before agents fan out. I would keep hooks minimal; for this scope, documented commands, role ownership, reports, and verification loops were enough without adding runtime machinery.
