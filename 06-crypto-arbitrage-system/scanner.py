from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Quote:
    exchange: str
    bid: Decimal
    ask: Decimal
    taker_fee: Decimal


def find_opportunity(quotes: list[Quote], min_net_spread_pct: Decimal = Decimal('0.20')):
    opportunities = []
    for buy in quotes:
        for sell in quotes:
            if buy.exchange == sell.exchange or buy.ask <= 0:
                continue

            gross = (sell.bid - buy.ask) / buy.ask * Decimal('100')
            fees = (buy.taker_fee + sell.taker_fee) * Decimal('100')
            net = gross - fees

            if net >= min_net_spread_pct:
                opportunities.append({
                    'buy_exchange': buy.exchange,
                    'sell_exchange': sell.exchange,
                    'buy_price': str(buy.ask),
                    'sell_price': str(sell.bid),
                    'gross_spread_pct': str(gross.quantize(Decimal('0.0001'))),
                    'estimated_net_pct': str(net.quantize(Decimal('0.0001'))),
                })

    return sorted(opportunities, key=lambda x: Decimal(x['estimated_net_pct']), reverse=True)


if __name__ == '__main__':
    demo_quotes = [
        Quote('EXCHANGE_A', Decimal('100.00'), Decimal('100.10'), Decimal('0.0005')),
        Quote('EXCHANGE_B', Decimal('100.60'), Decimal('100.70'), Decimal('0.0005')),
    ]
    print(find_opportunity(demo_quotes))
