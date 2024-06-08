#!/usr/bin/env python3
"""
Script that returns a tuple
"""

from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """Returns a list of integers multiplied by a factor"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Ensure factor is an integer
