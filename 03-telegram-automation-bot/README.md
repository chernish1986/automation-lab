# Telegram alert bot

A small Telegram notifier I keep for system tests and background jobs.

Typical use:

- send an alert when a script fails
- push a short status report
- forward an event from another service
- test message formatting before plugging it into a bigger bot

The bot reads its token/chat settings from environment variables. Nothing private is stored in the repository.

Status: public test build. It is meant to be changed for each service rather than used as-is.
