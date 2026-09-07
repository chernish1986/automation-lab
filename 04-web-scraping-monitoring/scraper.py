from dataclasses import dataclass, asdict
from hashlib import sha256
from typing import Iterable

from bs4 import BeautifulSoup


@dataclass(frozen=True)
class Record:
    title: str
    price: str

    @property
    def fingerprint(self) -> str:
        raw = f'{self.title}|{self.price}'.encode('utf-8')
        return sha256(raw).hexdigest()


def parse_records(html: str) -> list[Record]:
    soup = BeautifulSoup(html, 'html.parser')
    records = []
    for item in soup.select('[data-item]'):
        title = item.select_one('.title')
        price = item.select_one('.price')
        if title and price:
            records.append(Record(title.get_text(strip=True), price.get_text(strip=True)))
    return records


def deduplicate(records: Iterable[Record]) -> list[dict]:
    unique = {}
    for record in records:
        unique[record.fingerprint] = asdict(record)
    return list(unique.values())


if __name__ == '__main__':
    sample_html = '''<div data-item><span class="title">Test Item</span><span class="price">99.00</span></div>'''
    print(deduplicate(parse_records(sample_html)))
