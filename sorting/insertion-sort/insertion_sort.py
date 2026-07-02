"""
Insertion Sort
===============

In-place comparison sort that builds the sorted list one element at a
time, inserting each new element into its correct position among the
already-sorted elements.

Time Complexity:  O(n) best, O(n^2) average and worst case.
Space Complexity: O(1)
Stable:            Yes
"""

from __future__ import annotations
from typing import List, TypeVar

T = TypeVar("T", int, float, str)


def insertion_sort(arr: List[T]) -> List[T]:
    """
    Sort a list in ascending order using insertion sort.

    Args:
        arr: List of comparable elements to sort.

    Returns:
        The same list, sorted in place.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr