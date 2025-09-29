from __future__ import annotations

from typed_linq_collections.collections.numeric.q_int_types import QIntList, QIntOrderedIterable


def test_order_by_returns_q_int_ordered_iterable() -> None:
    assert isinstance(QIntList([3, 1, 2])
                      .order_by(lambda x: x),
                      QIntOrderedIterable)

def test_order_by_descending_returns_q_int_ordered_iterable() -> None:
    assert isinstance(QIntList([1, 3, 2])
                      .order_by_descending(lambda x: x),
                      QIntOrderedIterable)

def test_order_by_sorts_in_ascending_order() -> None:
    assert (QIntList([3, 1, 2])
            .order_by(lambda x: x)
            .to_list() == [1, 2, 3])

def test_order_by_descending_sorts_in_descending_order() -> None:
    assert (QIntList([1, 3, 2])
            .order_by_descending(lambda x: x)
            .to_list() == [3, 2, 1])

def test_then_by_sorts_in_ascending_order_as_secondary_sort() -> None:
    assert ((QIntList([31, 22, 21, 32])
             .order_by(lambda x: x // 10)  # sort by first digit
             .then_by(lambda x: x % 10))  # then by second digit
            .to_list() == [21, 31, 22, 32])

def test_then_by_descending_sorts_in_descending_order_as_secondary_sort() -> None:
    assert ((QIntList([31, 22, 21, 32])
             .order_by(lambda x: x // 10)  # sort by first digit
             .then_by_descending(lambda x: x % 10))  # then by second digit descending
            .to_list() == [22, 32, 21, 31])
