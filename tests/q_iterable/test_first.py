from __future__ import annotations

from test_common_helpers import throws_test, value_test_including_unordered_collections


def test_first_returns_first_value() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.first(),
                                               1)

def test_first_returns_single_none_value() -> None:
    value_test_including_unordered_collections([None],
                                               lambda x: x.first(),
                                               None)


def test_first_throws_if_no_values() -> None:
    throws_test([], lambda x: x.first())
