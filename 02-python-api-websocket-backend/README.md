# WebSocket backend test

Small async backend I use for checking API + WebSocket behaviour before moving the same logic into a larger service.

Main things covered here:

- HTTP health endpoint
- WebSocket connection handling
- simple event broadcast
- async task lifecycle
- disconnect cleanup
- basic logging

Run:

```bash
uvicorn app:app --reload
```

Then open the health endpoint or connect a WebSocket client to the configured route.

Status: test service. Good enough for local/VPS checks, not hardened for public production traffic.
