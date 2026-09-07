# Store reconciliation test

A stripped-down reconciliation script for checking daily store totals and mismatches.

The original use case was simple: take per-store numbers, compare expected vs actual balance and show where the difference came from.

Current checks:

- per-store totals
- expected vs actual balance
- discrepancy amount
- combined network total
- simple output that can later be written to CSV/DB/reporting

The sample values are fake and safe to publish.

Status: working test utility. Real deployments normally add database access, user permissions and a reporting layer around this calculation.
