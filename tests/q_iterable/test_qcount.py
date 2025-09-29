from __future__ import annotations

from test_common_helpers import lists_value_test


def test_single_element() -> None:
    lists_value_test([0],
                     lambda x: x.qcount(),
                     1)


def test_two_elements() -> None:
    lists_value_test([0, 3],
                     lambda x: x.qcount(),
                     2)


def test_three_elements() -> None:
    lists_value_test([0, 3, 5],
                     lambda x: x.qcount(),
                     3)


def test_predicate_exactly_zero() -> None:
    lists_value_test([0, 1, 2, 0],
                     lambda x: x.qcount(lambda v: v == 0),
                     2)


def test_predicate_not_none() -> None:
    lists_value_test([None, 1, None, 2],
                     lambda x: x.qcount(lambda v: v is not None),
                     2)


def test_predicate_is_string() -> None:
    lists_value_test(["a", 1, "b", 2],
                     lambda x: x.qcount(lambda v: isinstance(v, str)),
                     2)


def test_predicate_is_true() -> None:
    lists_value_test([True, False, True],
                     lambda x: x.qcount(lambda v: v is True),
                     2)


def test_predicate_empty_string() -> None:
    lists_value_test(["", "a", "", "b"],
                     lambda x: x.qcount(lambda v: v == ""),
                     2)


def test_predicate_empty_list() -> None:
    lists_value_test([],
                     lambda x: x.qcount(lambda v: v is not None),
                     0)
