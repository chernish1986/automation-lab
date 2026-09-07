# dev notes

Things I still want to check here:

- add reconnect jitter to the stream worker
- keep WebSocket messages bounded if producer is faster than consumer
- move Telegram retries into a small queue
- load scraper selectors from config instead of hardcoding them
- write reconciliation output to sqlite/csv
- add spread filter for minimum order-book depth
- keep every external action in dry-run by default

Nothing in this repo should require real credentials just to run a local test.
