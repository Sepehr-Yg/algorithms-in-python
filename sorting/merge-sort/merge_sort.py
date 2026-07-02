"""
Merge Sort
===========

Divide-and-conquer comparison sort that recursively splits the list into
halves, sorts each half, and merges the sorted halves back together.

Time Complexity:  O(n log n) best, average, and worst case.
Space Complexity: O(n)
Stable:            Yes
"""

from __future__ import annotations
from typing import List, TypeVar

T = TypeVar("T", int, float, str)


def merge_sort(arr: List[T]) -> List[T]:
    """
    Sort a list in ascending order using merge sort.

    Args:
        arr: List of comparable elements to sort.

    Returns:
        A new list containing all elements of ``arr`` in sorted order.
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)


def _merge(left: List[T], right: List[T]) -> List[T]:
    """Merge two sorted lists into a single sorted list."""
    merged: List[T] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged