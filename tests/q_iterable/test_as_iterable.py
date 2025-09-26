from __future__ import annotations

from typed_linq_collections.q_iterable import query


def test_returns_self() -> None:
    iterable = query([1, 2, 3])
    assert iterable.as_iterable() is iterable
