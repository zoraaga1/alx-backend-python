#!/usr/bin/env python3
"""Script that returns a list of tuples"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element in lst"""
    return [(i, len(i)) for i in lst]
