from __future__ import annotations

from test_common_helpers import throws_test, value_test_including_unordered_collections


def test_returns_first_value() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.first(),
                                               1)

def test_returns_single_none_value() -> None:
    value_test_including_unordered_collections([None],
                                               lambda x: x.first(),
                                               None)


def test_throws_if_no_values() -> None:
    throws_test([], lambda x: x.first())

def test_with_predicate_returns_first_matching_value() -> None:
    value_test_including_unordered_collections([1, 2, 3, 4],
                                               lambda x: x.first(lambda v: v % 2 == 0),
                                               2)

def test_with_predicate_returns_none_if_single_none_matches() -> None:
    value_test_including_unordered_collections([None, 1, 2],
                                               lambda x: x.first(lambda v: v is None),
                                               None)

def test_with_predicate_throws_if_no_match() -> None:
    throws_test([1, 2, 3],
                lambda x: x.first(lambda v: v > 10))
