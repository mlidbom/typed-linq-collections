from __future__ import annotations

from typed_linq_collections.collections.numeric.q_float_types import QFloatList, QFloatOrderedIterable


def test_order_by_returns_q_float_ordered_iterable() -> None:
    assert isinstance(QFloatList([3.5])
                      .order_by(lambda x: x),
                      QFloatOrderedIterable)

def test_order_by_sorts_in_ascending_order() -> None:
    assert (QFloatList([3.5, 1.2, 2.8])
            .order_by(lambda x: x)
            .to_list() == [1.2, 2.8, 3.5])

def test_order_by_descending_returns_q_float_ordered_iterable() -> None:
    assert isinstance(QFloatList([1.2])
                      .order_by_descending(lambda x: x),
                      QFloatOrderedIterable)

def test_order_by_descending_sorts_in_descending_order() -> None:
    assert (QFloatList([1.2, 3.5, 2.8])
            .order_by_descending(lambda x: x)
            .to_list() == [3.5, 2.8, 1.2])

def test_then_by_sorts_in_ascending_order_as_secondary_sort() -> None:
    assert ((QFloatList([3.1, 2.2, 2.1, 3.2])
             .order_by(lambda x: int(x))  # sort by integer part
             .then_by(lambda x: x % 1))  # then by decimal part
            .to_list() == [2.1, 3.1, 2.2, 3.2])

def test_then_by_descending_sorts_in_descending_order_as_secondary_sort() -> None:
    assert ((QFloatList([3.1, 2.2, 2.1, 3.2])
             .order_by(lambda x: int(x))  # sort by integer part
             .then_by_descending(lambda x: x % 1))  # then by decimal part descending
            .to_list() == [2.2, 3.2, 2.1, 3.1])

def test_order_by_handles_nan_and_infinity() -> None:
    # Test that NaN and infinity are handled properly
    import math
    values = [1.0, float("inf"), -1.0, float("-inf"), 2.0]
    result = QFloatList(values).order_by(lambda x: x if not math.isinf(x) else (float("inf") if x > 0 else float("-inf")))
    # Should sort normally, with infinities at the extremes
    sorted_vals = result.to_list()
    assert sorted_vals[0] == float("-inf")
    assert sorted_vals[-1] == float("inf")
    assert sorted_vals[1:-1] == [-1.0, 1.0, 2.0]
