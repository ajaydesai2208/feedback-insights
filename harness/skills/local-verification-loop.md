# Local Verification Loop

Use this workflow while implementing local-only features.

1. Identify the narrowest behavior to validate.
2. Run the smallest relevant command.
3. Fix failures close to the source.
4. Repeat until the command passes.
5. Record non-obvious failures or decisions in `LOGS.md`.

Avoid broad verification until the slice is stable.
