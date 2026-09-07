# Telegram alert bot

Small notifier for system checks and background jobs.

Typical use:

- send an alert when a script fails
- push a short status report
- forward an event from another service
- test message formatting before plugging it into a bigger bot

Settings are read from environment variables. Nothing private is stored here.

Status: public test build. I usually change the message source and retry logic depending on the service.
