from __future__ import annotations

from fractions import Fraction
from typing import TYPE_CHECKING

import pytest

from typed_linq_collections.collections.numeric.q_fraction_types import QFractionIterable, QFractionIterableImplementation
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query

if TYPE_CHECKING:
    from collections.abc import Iterable


def test_sum_returns_sum_of_the_values() -> None:
    assert query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().sum() == Fraction(6)

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_fractions().sum() == Fraction(0)

def test_min_returns_min_of_the_values() -> None:
    assert query([Fraction(6), Fraction(2), Fraction(5), Fraction(3)]).as_fractions().min() == Fraction(2)

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_fractions().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([Fraction(1), Fraction(5), Fraction(3)]).as_fractions().max() == Fraction(5)

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_fractions().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([Fraction(6), Fraction(2), Fraction(5), Fraction(3)]).as_fractions().min_or_default() == Fraction(2)

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_fractions().min_or_default() == Fraction(0)

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([Fraction(1), Fraction(5), Fraction(3)]).as_fractions().max_or_default() == Fraction(5)

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_fractions().max_or_default() == Fraction(0)

def test_average_returns_average_of_the_values() -> None:
    assert query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().average() == Fraction(2)

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_fractions().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().average_or_default() == Fraction(2)

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_fractions().average_or_default() == Fraction(0)

def test_where_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().where(lambda x: x > Fraction(2))
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(3), Fraction(4)]

def test_qfraction_iterable_implementation_constructor() -> None:
    def factory() -> Iterable[Fraction]:
        return iter([Fraction(1), Fraction(2), Fraction(3)])

    impl = QFractionIterableImplementation(factory)
    assert list(impl) == [Fraction(1), Fraction(2), Fraction(3)]
    assert isinstance(impl, QFractionIterable)
