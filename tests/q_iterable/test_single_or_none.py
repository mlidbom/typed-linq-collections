from __future__ import annotations

import pytest
from test_common_helpers import throws_test, value_test_including_unordered_collections

from typed_linq_collections.q_errors import InvalidOperationError
from typed_linq_collections.q_iterable import query


def test_returns_single_value() -> None:
    value_test_including_unordered_collections([1],
                                               lambda x: x.single_or_none(),
                                               1)


def test_returns_none_if_no_values() -> None:
    value_test_including_unordered_collections([],
                                               lambda x: x.single_or_none(),
                                               None)


def test_throws_if_multiple_values() -> None:
    throws_test([1, 2],
                lambda x: x.single_or_none(),
                InvalidOperationError)


def test_with_predicate_returns_single_value() -> None:
    assert query([1, 2, 3]).single_or_none(lambda x: x == 2) == 2


def test_with_predicate_returns_none_if_no_match() -> None:
    assert query([1, 2, 3]).single_or_none(lambda x: x == 4) is None


def test_with_predicate_throws_if_multiple_matches() -> None:
    with pytest.raises(InvalidOperationError):
        query([1, 2, 2, 3]).single_or_none(lambda x: x == 2)
