from __future__ import annotations

import pytest
from test_common_helpers import throws_test, value_test_including_unordered_collections

from typed_linq_collections.collections.numeric.q_int_types import QIntSet
from typed_linq_collections.q_errors import EmptyIterableError


def test_cast_int_returns_an_q_iterable_int_with_the_same_elements() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.cast.int().to_set(),
                                               {1, 2, 3})

def test_cast_checked_int_returns_a_q_iterable_int_with_the_same_elements() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.cast.checked.int().to_set(),
                                               {1, 2, 3})

def test_cast_checked_int_raises_type_error_if_collection_contains_non_int() -> None:
    throws_test([1, "2", 3],
                lambda x: x.cast.checked.int().to_set(),
                TypeError)

def test_sum_returns_sum_of_the_values() -> None:
    assert QIntSet([1, 2, 3]).sum() == 6

def test_sum_returns_zero_on_on_empty_collection() -> None:
    assert QIntSet().sum() == 0

def test_min_returns_min_of_the_values() -> None:
    assert QIntSet([6, 2, 5, 3]).min() == 2

def test_min_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QIntSet().min()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert QIntSet([6, 2, 5, 3]).min_or_default() == 2

def test_min_or_default_returns_0_on_on_empty_collection() -> None:
    assert QIntSet().min_or_default() == 0

def test_max_returns_max_of_the_values() -> None:
    assert QIntSet([1, 5, 3]).max() == 5

def test_max_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QIntSet().max()

def test_max_or_default_returns_max_of_the_values() -> None:
    assert QIntSet([1, 5, 3]).max_or_default() == 5

def test_max_or_default_returns_0_on_on_empty_collection() -> None:
    assert QIntSet().max_or_default() == 0

def test_average_returns_average_of_the_values() -> None:
    assert QIntSet([1, 2, 3]).average() == 2

def test_average_throws_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QIntSet().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert QIntSet([1, 2, 3]).average_or_default() == 2

def test_average_or_default_returns_0_on_on_empty_collection() -> None:
    assert QIntSet().average_or_default() == 0

def test_to_set_returns_a_set_with_the_same_elements() -> None:
    assert QIntSet([1, 2, 3]).to_set() == {1, 2, 3}

def test_constructor_with_no_arguments_creates_empty_collection() -> None:
    empty_set = QIntSet()
    assert len(empty_set) == 0
    assert set(empty_set) == set()
