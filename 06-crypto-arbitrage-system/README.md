# Cross-exchange spread scanner

Test scanner for comparing prices between exchanges and checking whether a raw spread is still interesting after fees/funding assumptions.

I keep this separate from any live trading code. It is useful for checking calculation logic without API keys or order execution.

Current checks:

- best buy / best sell venue
- raw spread %
- estimated fees
- optional funding adjustment
- simple threshold filter

No real account credentials or order placement are included here.

Status: calculation/scanner test only. Before using the same idea for live trading it needs exchange-specific precision rules, liquidity checks, execution/reconciliation and risk controls.
