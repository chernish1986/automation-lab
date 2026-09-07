# automation-lab

Small public test utilities I keep around for integration work, API checks and automation experiments.

Most of this code is intentionally simple. The point is to have working pieces that can be run, changed and reused when I need to test an idea quickly.

Current folders:

- `01-ai-business-automation` — webhook -> AI/API routing experiments
- `02-python-api-websocket-backend` — async API/WebSocket service checks
- `03-telegram-automation-bot` — Telegram alerts and event delivery
- `04-web-scraping-monitoring` — extraction/change-monitoring scripts
- `05-retail-network-automation` — store balance/reconciliation calculations
- `06-crypto-arbitrage-system` — spread/funding/fee calculation tests

## Running

Python 3.10+ is enough for the Python utilities.

```bash
pip install -r requirements.txt
```

Each folder has its own notes and entry point.

## Status

These are public test builds, not production deployments. Credentials, private endpoints and real account data are not stored here.

Some ideas were tested against open-source implementations. References and licenses are kept in `OPEN_SOURCE_REFERENCES.md`.
