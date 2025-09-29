from __future__ import annotations

import pytest
from test_common_helpers import throws_test, value_test_including_unordered_collections

from typed_linq_collections.collections.numeric.q_int_types import QIntFrozenSet
from typed_linq_collections.q_errors import EmptyIterableError


def test_cast_int_returns_an_q_iterable_int_with_the_same_elements() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.cast.int().to_frozenset(),
                                               frozenset({1, 2, 3}))

def test_cast_checked_int_returns_a_q_iterable_int_with_the_same_elements() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.cast.checked.int().to_frozenset(),
                                               frozenset({1, 2, 3}))

def test_cast_checked_int_raises_type_error_if_collection_contains_non_int() -> None:
    throws_test([1, "2", 3],
                lambda x: x.cast.checked.int().to_frozenset(),
                TypeError)

def test_sum_returns_sum_of_the_values() -> None: assert QIntFrozenSet([1, 2, 3]).sum() == 6
def test_sum_returns_zero_on_on_empty_collection() -> None: assert QIntFrozenSet().sum() == 0

def test_min_returns_min_of_the_values() -> None: assert QIntFrozenSet([6, 2, 5, 3]).min() == 2
def test_min_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QIntFrozenSet().min()

def test_min_or_default_returns_min_of_the_values() -> None: assert QIntFrozenSet([6, 2, 5, 3]).min_or_default() == 2
def test_min_or_default_returns_0_on_on_empty_collection() -> None: assert QIntFrozenSet().min_or_default() == 0

def test_max_returns_max_of_the_values() -> None: assert QIntFrozenSet([1, 5, 3]).max() == 5
def test_max_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QIntFrozenSet().max()

def test_max_or_default_returns_max_of_the_values() -> None: assert QIntFrozenSet([1, 5, 3]).max_or_default() == 5
def test_max_or_default_returns_0_on_on_empty_collection() -> None: assert QIntFrozenSet().max_or_default() == 0

def test_average_returns_average_of_the_values() -> None: assert QIntFrozenSet([1, 2, 3]).average() == 2
def test_average_throws_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QIntFrozenSet().average()

def test_average_or_default_returns_average_of_the_values() -> None: assert QIntFrozenSet([1, 2, 3]).average_or_default() == 2
def test_average_or_default_returns_0_on_on_empty_collection() -> None: assert QIntFrozenSet().average_or_default() == 0

def test_to_frozenset_returns_a_frozenset_with_the_same_elements() -> None: assert QIntFrozenSet([1, 2, 3]).to_frozenset() == frozenset({1, 2, 3})
