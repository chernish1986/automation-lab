# Scraper / change monitor

Small scraper used for testing extraction and change-detection logic on public pages.

Things I normally check with it:

- selectors still work
- values are normalized correctly
- duplicates are removed
- changed values are detected
- results can be passed to another process

The script is intentionally small so it is easy to change for a new source.

Status: test utility. Check the target site's terms, robots rules and request limits before using it against a real source.
