from dataclasses import dataclass
from decimal import Decimal


@dataclass
class StoreBalance:
    store: str
    expected: Decimal
    actual: Decimal

    @property
    def difference(self) -> Decimal:
        return self.actual - self.expected


def reconcile(rows: list[StoreBalance], tolerance: Decimal = Decimal('0.01')) -> dict:
    discrepancies = []
    total_expected = Decimal('0')
    total_actual = Decimal('0')

    for row in rows:
        total_expected += row.expected
        total_actual += row.actual
        if abs(row.difference) > tolerance:
            discrepancies.append({
                'store': row.store,
                'expected': str(row.expected),
                'actual': str(row.actual),
                'difference': str(row.difference),
            })

    return {
        'total_expected': str(total_expected),
        'total_actual': str(total_actual),
        'network_difference': str(total_actual - total_expected),
        'discrepancies': discrepancies,
    }


if __name__ == '__main__':
    demo = [
        StoreBalance('Store A', Decimal('1250.00'), Decimal('1250.00')),
        StoreBalance('Store B', Decimal('980.50'), Decimal('978.00')),
    ]
    print(reconcile(demo))
