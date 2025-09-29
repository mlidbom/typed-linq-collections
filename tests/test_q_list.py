from __future__ import annotations

from typed_linq_collections.collections.q_list import QList


def test_q_list_empty_constructor() -> None:
    empty_list = QList()
    assert len(empty_list) == 0
    assert empty_list.to_list() == []


def test_q_list_with_iterable() -> None:
    test_list = QList([1, 2, 3])
    assert len(test_list) == 3
    assert test_list.to_list() == [1, 2, 3]


def test_q_list_element_at() -> None:
    test_list = QList([1, 2, 3])
    assert test_list.element_at(0) == 1
    assert test_list.element_at(1) == 2
    assert test_list.element_at(2) == 3


def test_q_list_indexing() -> None:
    test_list = QList([1, 2, 3, 4, 5])
    assert test_list[1] == 2

    # Test slice returning QList
    sliced = test_list[1:4]
    assert isinstance(sliced, QList)
    assert sliced.to_list() == [2, 3, 4]
