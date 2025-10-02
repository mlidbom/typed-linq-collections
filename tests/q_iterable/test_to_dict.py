from __future__ import annotations

import pytest

from typed_linq_collections.collections.q_list import QList
from typed_linq_collections.q_iterable import query


class DummyObj:
    def __init__(self, name: str, val: int) -> None:
        self.name: str = name
        self.val: int = val

def test_to_dict_with_selectors_returns_a_dict_combining_the_selected_keys_and_values() -> None:
    assert (query([DummyObj("x", 10),
                   DummyObj("y", 14),
                   DummyObj("z", 16)])
            .to_dict(lambda o: o.name, lambda o: o.val) == {"x": 10,
                                                            "y": 14,
                                                            "z": 16})

def test_to_dict_with_selectors_on_empty_sequence_returns_empty_dict() -> None:
    assert QList[int]([]).to_dict(lambda x: x, lambda x: x) == {}

def test_to_dict_with_selectors_on_single_item_returns_single_entry_dict() -> None:
    assert (query([(DummyObj("test", 42))])
            .to_dict(lambda o: o.name, lambda o: o.val) == {"test": 42})

def test_to_dict_with_duplicate_keys_raises_value_error_by_default() -> None:
    """Test that duplicate keys raise ValueError by default (.NET behavior)."""
    with pytest.raises(ValueError, match="An element with the same key already exists: same"):
        query([DummyObj("same", 1),
               DummyObj("same", 2),
               DummyObj("same", 3)]).to_dict(lambda o: o.name, lambda o: o.val)

def test_to_dict_with_duplicate_keys_and_allow_duplicates_uses_last_value() -> None:
    """Test that when allow_duplicates=True, last value wins (Python dict behavior)."""
    assert (query([DummyObj("same", 1),
                   DummyObj("same", 2),
                   DummyObj("same", 3)])
            .to_dict(lambda o: o.name, lambda o: o.val, allow_duplicates=True) == {"same": 3})

def test_to_dict_with_multiple_duplicate_keys_raises_on_first_duplicate() -> None:
    """Test that ValueError is raised on the first duplicate key encountered."""
    with pytest.raises(ValueError, match="An element with the same key already exists: a"):
        query([DummyObj("a", 1),
               DummyObj("b", 2),
               DummyObj("a", 3),  # First duplicate
               DummyObj("c", 4),
               DummyObj("b", 5)]).to_dict(lambda o: o.name, lambda o: o.val)

def test_to_dict_allow_duplicates_false_explicitly() -> None:
    """Test that explicitly setting allow_duplicates=False raises on duplicates."""
    with pytest.raises(ValueError, match="An element with the same key already exists: key"):
        query([("key", "val1"), ("key", "val2")]).to_dict(lambda x: x[0], lambda x: x[1], allow_duplicates=False)

def test_to_dict_with_none_keys_allows_duplicates_when_enabled() -> None:
    """Test that None keys work correctly with allow_duplicates=True."""
    result = query([(None, 1), (None, 2), ("key", 3)]).to_dict(
        lambda x: x[0], lambda x: x[1], allow_duplicates=True)
    assert result == {None: 2, "key": 3}

def test_to_dict_with_none_keys_raises_on_duplicates_by_default() -> None:
    """Test that None keys raise ValueError on duplicates by default."""
    with pytest.raises(ValueError, match="An element with the same key already exists: None"):
        query([(None, 1), (None, 2)]).to_dict(lambda x: x[0], lambda x: x[1])
