# AI workflow test

Old test flow for checking a simple business automation chain:

`webhook -> normalize input -> AI classification -> route -> external action`

The JSON is kept here because it is useful when I need to rebuild the same pattern in n8n without starting from zero.

## What I usually check

- incoming webhook payloads
- JSON cleanup before the AI call
- category / priority response format
- routing by result
- retry path when an API returns bad JSON
- notification step after processing

`workflow.json` does not contain credentials or real customer data.

Status: usable as a test flow, needs real credentials/endpoints before connecting to any live service.
