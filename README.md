# automation-lab

Public test utilities for API checks, automation ideas and small integration jobs.

I keep these scripts simple on purpose. They are easier to reuse when I need to test one part of a bigger system without pulling in the whole project.

Current workbench:

- `lead-router/` — webhook + AI/API routing test
- `stream-worker/` — async event/WebSocket worker
- `tg-alerts/` — Telegram notifier with dry-run mode
- `page-watch/` — small extraction/change-check script
- `store-reconcile/` — balance/reconciliation calculator
- `spread-check/` — cross-exchange spread math

## Setup

Python 3.10+.

```bash
pip install -r requirements.txt
cp .env.example .env
```

On Windows just copy `.env.example` to `.env` manually.

## Notes

Everything here should run without real credentials in test/dry-run mode. Private endpoints, production configs and account data stay outside the repository.

Rough TODOs and things I still want to check are in `dev_notes.md`.

Third-party repos checked while comparing approaches are listed in `third_party.md`.
