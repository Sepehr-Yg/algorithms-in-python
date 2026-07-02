"""
Selection Sort
===============

In-place comparison sort that repeatedly selects the smallest remaining
element and moves it to its correct position.

Time Complexity:  O(n^2) best, average, and worst case.
Space Complexity: O(1)
Stable:            No
"""

from __future__ import annotations
from typing import List, TypeVar

T = TypeVar("T", int, float, str)


def selection_sort(arr: List[T]) -> List[T]:
    """
    Sort a list in ascending order using selection sort.

    Args:
        arr: List of comparable elements to sort.

    Returns:
        The same list, sorted in place.
    """
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr