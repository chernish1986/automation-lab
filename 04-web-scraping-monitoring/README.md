# Scraper / change monitor

Small scraper used for testing extraction and change-detection logic on public pages.

It is useful for quick checks when I need to confirm:

- selectors still work
- values are normalized correctly
- duplicates are removed
- a changed value is detected
- results can be saved or passed to another process

The script is intentionally small so it is easy to modify for a new source.

Status: test utility. Respect the target site's terms, robots rules and request limits before using it against a real source.
