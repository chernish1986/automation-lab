# Store reconciliation test

Stripped-down reconciliation script for checking daily store totals and mismatches.

The basic job is simple: take per-store numbers, compare expected vs actual balance and show where the difference came from.

Current checks:

- per-store totals
- expected vs actual balance
- discrepancy amount
- combined network total
- output that can later be written to CSV/DB/reporting

The sample values are fake and safe to publish.

Status: working test utility. Real deployments usually add database access, permissions and reporting around this calculation.
