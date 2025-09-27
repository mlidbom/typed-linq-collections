from __future__ import annotations

from test_common_helpers import value_test_including_unordered_collections

from typed_linq_collections.q_iterable import query


def test_any_returns_true_if_there_are_elements() -> None:
    value_test_including_unordered_collections([1],
                                               lambda x: x.any(),
                                               True)


def test_any_returns_false_if_there_are_no_elements() -> None:
    value_test_including_unordered_collections([],
                                               lambda x: x.any(),
                                               False)


def test_with_predicate_returns_true_if_any_match() -> None:
    items = query([1, 2, 3, 4])
    assert items.any(lambda x: x % 2 == 0) is True  # 2 and 4 are even


def test_with_predicate_returns_false_if_no_match() -> None:
    items = query([1, 3, 5])
    assert items.any(lambda x: x % 2 == 0) is False  # no even numbers


def test_any_with_predicate_on_empty_iterable_returns_false() -> None:
    items = query(list[int]())
    assert items.any(lambda x: True) is False  # empty, so no match


def test_with_predicate_returns_true_for_first_match() -> None:
    items = query([0, 0, 1])
    assert items.any(lambda x: x == 1) is True


def test_any_with_predicate_returns_false_for_all_false() -> None:
    items = query([0, 0, 0])
    assert items.any(lambda x: x == 1) is False
