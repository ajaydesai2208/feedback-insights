# Eval Report

Generated: 2026-05-04 20:47:46 UTC
Model: `gpt-4o-mini`
Status: completed

## Summary

- Cases: 8
- Sentiment exact match: 7/8
- Average theme overlap: 0.71
- Average action intent score: 0.75
- Malformed outputs: 0
- Provider failures: 0

## Case Results

| Case | Sentiment | Theme overlap | Action intent | Malformed/failure |
| --- | --- | ---: | ---: | --- |
| `positive-onboarding-001` | pass | 0.67 | 1.00 |  |
| `negative-billing-002` | pass | 0.67 | 0.00 |  |
| `neutral-status-003` | pass | 1.00 | 1.00 |  |
| `mixed-mobile-004` | pass | 0.67 | 1.00 |  |
| `feature-request-slack-005` | fail | 0.67 | 1.00 |  |
| `support-process-006` | pass | 0.67 | 1.00 |  |
| `product-usability-007` | pass | 1.00 | 0.00 |  |
| `cx-renewal-008` | pass | 0.33 | 1.00 |  |

## Notes

Theme overlap is token-based and intentionally approximate.
Action intent scoring checks whether expected request intent appears in extracted action items.
Failures here should guide prompt/schema changes; this runner does not edit app prompts.
