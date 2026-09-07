import asyncio
import json
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('realtime-backend')


@dataclass
class Event:
    source: str
    payload: dict


class RealtimeService:
    def __init__(self):
        self.queue: asyncio.Queue[Event] = asyncio.Queue()
        self.running = True

    async def ingest(self):
        delay = 1
        while self.running:
            try:
                await asyncio.sleep(1)
                await self.queue.put(Event('test-stream', {'type': 'heartbeat'}))
                delay = 1
            except Exception as exc:
                log.exception('stream error: %s', exc)
                await asyncio.sleep(delay)
                delay = min(delay * 2, 30)

    async def process(self):
        while self.running:
            event = await self.queue.get()
            try:
                log.info('source=%s event=%s', event.source, json.dumps(event.payload, sort_keys=True))
            finally:
                self.queue.task_done()


async def main():
    service = RealtimeService()
    await asyncio.gather(service.ingest(), service.process())


if __name__ == '__main__':
    asyncio.run(main())
