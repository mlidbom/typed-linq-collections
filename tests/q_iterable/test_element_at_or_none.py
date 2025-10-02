from __future__ import annotations

from test_common_helpers import value_test_including_unordered_collections


def test_0_test_returns_element_1() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.element_at_or_none(0),
                                               1)

def test_1_return_element_2() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.element_at_or_none(1),
                                               2)

def test_2_returns_element_3() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.element_at_or_none(2),
                                               3)

def test_returns_none_if_index_is_out_of_range() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.element_at_or_none(3),
                                               None)

def test_returns_none_if_index_is_negative_one() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.element_at_or_none(-1),
                                               None)

def test_returns_none_if_index_is_negative_five() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.element_at_or_none(-5),
                                               None)

def test_returns_none_if_index_is_negative_on_empty_collection() -> None:
    value_test_including_unordered_collections([],
                                               lambda x: x.element_at_or_none(-1),
                                               None)

def test_returns_none_if_index_is_zero_on_empty_collection() -> None:
    value_test_including_unordered_collections([],
                                               lambda x: x.element_at_or_none(0),
                                               None)
