from __future__ import annotations

import pytest
from test_common_helpers import throws_test, value_test_including_unordered_collections

from typed_linq_collections.collections.numeric.q_float_types import QFloatSequence
from typed_linq_collections.q_errors import EmptyIterableError


def test_cast_float_returns_an_q_iterable_float_with_the_same_elements() -> None:
    value_test_including_unordered_collections([1.1, 2.1, 3.1],
                                               lambda x: x.cast.float().to_sequence().to_list(),
                                               [1.1, 2.1, 3.1])

def test_cast_checked_float_returns_a_q_iterable_float_with_the_same_elements() -> None:
    value_test_including_unordered_collections([1.1, 2.1, 3.1],
                                               lambda x: x.cast.checked.float().to_sequence().to_list(),
                                               [1.1, 2.1, 3.1])

def test_cast_checked_float_raises_type_error_if_collection_contains_non_float() -> None:
    throws_test([1.1, "2.1", 3.1],
                lambda x: x.cast.checked.float().to_sequence(),
                TypeError)

def test_sum_returns_sum_of_the_values() -> None: assert QFloatSequence([1.1, 2.1, 3.1]).sum() == pytest.approx(6.3)  # pyright: ignore [reportUnknownMemberType]
def test_sum_returns_zero_on_on_empty_collection() -> None: assert QFloatSequence().sum() == 0

def test_min_returns_min_of_the_values() -> None: assert QFloatSequence([6.1, 2.1, 5.1, 3.1]).min() == 2.1
def test_min_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QFloatSequence().min()

def test_min_or_default_returns_min_of_the_values() -> None: assert QFloatSequence([6.1, 2.1, 5.1, 3.1]).min_or_default() == 2.1
def test_min_or_default_returns_0_on_on_empty_collection() -> None: assert QFloatSequence().min_or_default() == 0

def test_max_returns_max_of_the_values() -> None: assert QFloatSequence([1.1, 5.1, 3.1]).max() == 5.1
def test_max_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QFloatSequence().max()

def test_max_or_default_returns_max_of_the_values() -> None: assert QFloatSequence([1.1, 5.1, 3.1]).max_or_default() == 5.1
def test_max_or_default_returns_0_on_on_empty_collection() -> None: assert QFloatSequence().max_or_default() == 0

def test_average_returns_average_of_the_values() -> None: assert QFloatSequence([1.1, 2.1, 3.1]).average() == 2.1
def test_average_throws_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QFloatSequence().average()

def test_average_or_default_returns_average_of_the_values() -> None: assert QFloatSequence([1.1, 2.1, 3.1]).average_or_default() == 2.1
def test_average_or_default_returns_0_on_on_empty_collection() -> None: assert QFloatSequence().average_or_default() == 0

def test_to_sequence_returns_a_sequence_with_the_same_elements() -> None: assert QFloatSequence([1.1, 2.1, 3.1]).to_sequence().to_list() == [1.1, 2.1, 3.1]
