from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from typed_linq_collections.collections.numeric.q_float_types import QFloatIterable, QFloatIterableImplementation
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query

if TYPE_CHECKING:
    from collections.abc import Iterable


def test_sum_returns_sum_of_the_values() -> None:
    assert query([1.0, 2.0, 3.0]).as_floats().sum() == 6.0

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_floats().sum() == 0.0

def test_min_returns_min_of_the_values() -> None:
    assert query([6.0, 2.0, 5.0, 3.0]).as_floats().min() == 2.0

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_floats().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([1.0, 5.0, 3.0]).as_floats().max() == 5.0

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_floats().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([6.0, 2.0, 5.0, 3.0]).as_floats().min_or_default() == 2.0

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_floats().min_or_default() == 0.0

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([1.0, 5.0, 3.0]).as_floats().max_or_default() == 5.0

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_floats().max_or_default() == 0.0

def test_average_returns_average_of_the_values() -> None:
    assert query([1.0, 2.0, 3.0]).as_floats().average() == 2.0

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_floats().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([1.0, 2.0, 3.0]).as_floats().average_or_default() == 2.0

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_floats().average_or_default() == 0.0

def test_where_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().where(lambda x: x > 2.0)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [3.0, 4.0]

def test_qfloat_iterable_implementation_constructor() -> None:
    def factory() -> Iterable[float]:
        return iter([1.0, 2.0, 3.0])

    impl = QFloatIterableImplementation(factory)
    assert list(impl) == [1.0, 2.0, 3.0]
    assert isinstance(impl, QFloatIterable)
