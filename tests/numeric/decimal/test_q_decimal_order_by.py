from __future__ import annotations

from decimal import Decimal

from typed_linq_collections.collections.numeric.q_decimal_types import QDecimalList, QDecimalOrderedIterable


def test_order_by_returns_q_decimal_ordered_iterable() -> None:
    assert isinstance(QDecimalList([Decimal("3.5")]).order_by(lambda x: x),
                      QDecimalOrderedIterable)

def test_order_by_descending_returns_q_decimal_ordered_iterable() -> None:
    assert isinstance((QDecimalList([Decimal("1.2")])
                       .order_by_descending(lambda x: x)), QDecimalOrderedIterable)

def test_order_by_sorts_in_ascending_order() -> None:
    assert (QDecimalList([Decimal("3.5"),
                          Decimal("1.2"),
                          Decimal("2.8")])
            .order_by(lambda x: x).to_list()
            == [Decimal("1.2"), Decimal("2.8"), Decimal("3.5")])

def test_order_by_descending_sorts_in_descending_order() -> None:
    assert (QDecimalList([Decimal("1.2"),
                          Decimal("3.5"),
                          Decimal("2.8")])
            .order_by_descending(lambda x: x).to_list()
            == [Decimal("3.5"),
                Decimal("2.8"),
                Decimal("1.2")])

def test_then_by_sorts_in_ascending_order_as_secondary_sort() -> None:
    assert ((QDecimalList([Decimal("3.1"),
                           Decimal("2.2"),
                           Decimal("2.1"),
                           Decimal("3.2")])
             .order_by(lambda x: int(x))  # sort by integer part
             .then_by(lambda x: x % 1))  # then by decimal part
            .to_list() == [Decimal("2.1"),
                           Decimal("3.1"),
                           Decimal("2.2"),
                           Decimal("3.2")])

def test_then_by_descending_sorts_in_descending_order_as_secondary_sort() -> None:
    assert ((QDecimalList([Decimal("3.1"),
                           Decimal("2.2"),
                           Decimal("2.1"),
                           Decimal("3.2")])
             .order_by(lambda x: int(x))  # sort by integer part
             .then_by_descending(lambda x: x % 1))  # then by decimal part descending
            .to_list() == [Decimal("2.2"),
                           Decimal("3.2"),
                           Decimal("2.1"),
                           Decimal("3.1")])
