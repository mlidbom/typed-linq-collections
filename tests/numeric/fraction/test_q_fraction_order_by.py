from __future__ import annotations

from fractions import Fraction

from typed_linq_collections.collections.numeric.q_fraction_types import QFractionList, QFractionOrderedIterable


def test_order_by_returns_q_fraction_ordered_iterable() -> None:
    assert isinstance(QFractionList([Fraction(3, 4)])
                      .order_by(lambda x: x),
                      QFractionOrderedIterable)

def test_order_by_descending_returns_q_fraction_ordered_iterable() -> None:
    assert isinstance(QFractionList([Fraction(1, 2)])
                      .order_by_descending(lambda x: x),
                      QFractionOrderedIterable)

def test_order_by_sorts_in_ascending_order() -> None:
    assert (QFractionList([Fraction(3, 4),
                           Fraction(1, 2),
                           Fraction(2, 3)])
            .order_by(lambda x: x)
            .to_list() == [Fraction(1, 2),
                           Fraction(2, 3),
                           Fraction(3, 4)])

def test_order_by_descending_sorts_in_descending_order() -> None:
    assert (QFractionList([Fraction(1, 2),
                           Fraction(3, 4),
                           Fraction(2, 3)])
            .order_by_descending(lambda x: x)
            .to_list() == [Fraction(3, 4),
                           Fraction(2, 3),
                           Fraction(1, 2)])

def test_then_by_sorts_in_ascending_order_as_secondary_sort() -> None:
    # Note: fractions are automatically reduced: 3/3 -> 1/1, 2/4 -> 1/2
    # After reduction: [3/4, 1/2, 2/3, 1/1] with numerators [3, 1, 2, 1] and denominators [4, 2, 3, 1]
    # Sort by numerator: [1/2, 1/1, 2/3, 3/4] (numerators: 1, 1, 2, 3)
    # Then by denominator: [1/1, 1/2, 2/3, 3/4] (denominators: 1, 2, 3, 4)
    assert ((QFractionList([Fraction(3, 4),
                            Fraction(2, 4),
                            Fraction(2, 3),
                            Fraction(3, 3)])
             .order_by(lambda x: x.numerator)  # sort by numerator
             .then_by(lambda x: x.denominator))  # then by denominator
            .to_list() == [Fraction(1, 1),
                           Fraction(1, 2),
                           Fraction(2, 3),
                           Fraction(3, 4)])

def test_then_by_descending_sorts_in_descending_order_as_secondary_sort() -> None:
    # After reduction: [3/4, 1/2, 2/3, 1/1]
    # Sort by numerator: [1/2, 1/1, 2/3, 3/4] (numerators: 1, 1, 2, 3) - stable sort
    # Then by denominator desc: [1/2, 1/1, 2/3, 3/4] -> [1/2, 1/1, 2/3, 3/4] (denominators desc: 2, 1, 3, 4)
    assert ((QFractionList([Fraction(3, 4),
                            Fraction(2, 4),
                            Fraction(2, 3),
                            Fraction(3, 3)])
             .order_by(lambda x: x.numerator)  # sort by numerator
             .then_by_descending(lambda x: x.denominator))  # then by denominator descending
            .to_list() == [Fraction(3, 4),
                           Fraction(2, 3),
                           Fraction(1, 2),
                           Fraction(1, 1)])