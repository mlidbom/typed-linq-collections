from __future__ import annotations

from fractions import Fraction

import pytest
from test_common_helpers import throws_test, value_test_including_unordered_collections

from typed_linq_collections.collections.numeric.q_fraction_types import QFractionSequence
from typed_linq_collections.q_errors import EmptyIterableError


def test_cast_fraction_returns_an_q_iterable_fraction_with_the_same_elements() -> None:
    value_test_including_unordered_collections([Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)],
                                               lambda x: x.cast.fraction().to_sequence().to_list(),
                                               [Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)])

def test_cast_checked_fraction_returns_a_q_iterable_fraction_with_the_same_elements() -> None:
    value_test_including_unordered_collections([Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)],
                                               lambda x: x.cast.checked.fraction().to_sequence().to_list(),
                                               [Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)])

def test_cast_checked_fraction_raises_type_error_if_collection_contains_non_fraction() -> None:
    throws_test([Fraction(11, 10), "2.1", Fraction(31, 10)], lambda x: x.cast.checked.fraction().to_sequence(), TypeError)

def test_sum_returns_sum_of_the_values() -> None: assert QFractionSequence([Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)]).sum() == Fraction(63, 10)
def test_sum_returns_zero_on_on_empty_collection() -> None: assert QFractionSequence().sum() == Fraction(0)

def test_min_returns_min_of_the_values() -> None: assert QFractionSequence([Fraction(61, 10), Fraction(21, 10), Fraction(51, 10), Fraction(31, 10)]).min() == Fraction(21, 10)
def test_min_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QFractionSequence().min()

def test_min_or_default_returns_min_of_the_values() -> None: assert QFractionSequence([Fraction(61, 10), Fraction(21, 10), Fraction(51, 10), Fraction(31, 10)]).min_or_default() == Fraction(21, 10)
def test_min_or_default_returns_0_on_on_empty_collection() -> None: assert QFractionSequence().min_or_default() == Fraction(0)

def test_max_returns_max_of_the_values() -> None: assert QFractionSequence([Fraction(11, 10), Fraction(51, 10), Fraction(31, 10)]).max() == Fraction(51, 10)
def test_max_raises_invalid_operation_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QFractionSequence().max()

def test_max_or_default_returns_max_of_the_values() -> None: assert QFractionSequence([Fraction(11, 10), Fraction(51, 10), Fraction(31, 10)]).max_or_default() == Fraction(51, 10)
def test_max_or_default_returns_0_on_on_empty_collection() -> None: assert QFractionSequence().max_or_default() == Fraction(0)

def test_average_returns_average_of_the_values() -> None: assert QFractionSequence([Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)]).average() == Fraction(21, 10)
def test_average_throws_on_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError): QFractionSequence().average()

def test_average_or_default_returns_average_of_the_values() -> None: assert QFractionSequence([Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)]).average_or_default() == Fraction(21, 10)
def test_average_or_default_returns_0_on_on_empty_collection() -> None: assert QFractionSequence().average_or_default() == Fraction(0)

def test_to_sequence_returns_a_sequence_with_the_same_elements() -> None: assert QFractionSequence([Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)]).to_sequence().to_list() == [Fraction(11, 10), Fraction(21, 10), Fraction(31, 10)]