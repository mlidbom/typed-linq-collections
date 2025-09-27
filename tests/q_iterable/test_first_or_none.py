from __future__ import annotations

from test_common_helpers import value_test_including_unordered_collections


def test__returns_first_value() -> None:
    value_test_including_unordered_collections([1, 2, 3],
                                               lambda x: x.first_or_none(),
                                               1)

def test_return_none_if_no_values() -> None:
    value_test_including_unordered_collections([],
                                               lambda x: x.first_or_none(),
                                               None)

def test_returns_single_none_value() -> None:
    value_test_including_unordered_collections([None],
                                               lambda x: x.first_or_none(),
                                               None)