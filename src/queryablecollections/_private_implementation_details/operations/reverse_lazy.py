from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def reverse_lazy[TItem](self: Iterable[TItem]) -> Iterable[TItem]:
    return reversed(list(self))
