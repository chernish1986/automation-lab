# Cross-exchange spread check

Small scanner for comparing prices between exchanges and checking whether a raw spread still makes sense after fee assumptions.

I keep this separate from live execution code. It is useful for checking the math without API keys or order placement.

Current checks:

- best buy / best sell venue
- raw spread %
- estimated taker fees
- simple net threshold

No real account credentials or order placement are included here.

Status: calculation test only. Live use needs exchange precision rules, liquidity checks, execution/reconciliation and risk controls.
