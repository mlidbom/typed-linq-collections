from __future__ import annotations

from decimal import Decimal

import pytest

from typed_linq_collections.collections.numeric.q_decimal_types import QDecimalIterable, QDecimalIterableImplementation
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query


def test_sum_returns_sum_of_the_values() -> None:
    assert query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().sum() == Decimal(6)

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_decimals().sum() == Decimal(0)

def test_min_returns_min_of_the_values() -> None:
    assert query([Decimal(6), Decimal(2), Decimal(5), Decimal(3)]).as_decimals().min() == Decimal(2)

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_decimals().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([Decimal(1), Decimal(5), Decimal(3)]).as_decimals().max() == Decimal(5)

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_decimals().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([Decimal(6), Decimal(2), Decimal(5), Decimal(3)]).as_decimals().min_or_default() == Decimal(2)

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_decimals().min_or_default() == Decimal(0)

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([Decimal(1), Decimal(5), Decimal(3)]).as_decimals().max_or_default() == Decimal(5)

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_decimals().max_or_default() == Decimal(0)

def test_average_returns_average_of_the_values() -> None:
    assert query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().average() == Decimal(2)

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_decimals().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().average_or_default() == Decimal(2)

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_decimals().average_or_default() == Decimal(0)

def test_where_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().where(lambda x: x > Decimal(2))
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(3), Decimal(4)]

def test_qdecimal_iterable_implementation_constructor() -> None:
    impl = QDecimalIterableImplementation(lambda: (Decimal(1), Decimal(2), Decimal(3)))
    assert list(impl) == [Decimal(1), Decimal(2), Decimal(3)]
    assert isinstance(impl, QDecimalIterable)
