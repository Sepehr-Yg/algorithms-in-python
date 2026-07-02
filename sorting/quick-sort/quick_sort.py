"""
Quick Sort
===========

Divide-and-conquer comparison sort that picks a pivot, partitions the
remaining elements around it, and recursively sorts each partition.

Time Complexity:  O(n log n) best/average, O(n^2) worst case.
Space Complexity: O(log n) average (recursion stack, in-place variant).
Stable:            No

Includes two implementations:
- quick_sort(): functional version using list comprehensions.
- quick_sort_in_place(): in-place version using Lomuto partitioning.
"""

from __future__ import annotations
from typing import List, TypeVar

T = TypeVar("T", int, float, str)


def quick_sort(arr: List[T]) -> List[T]:
    """
    Sort a list in ascending order using quicksort (functional version).

    Args:
        arr: List of comparable elements to sort.

    Returns:
        A new list containing all elements of ``arr`` in sorted order.
    """
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


def quick_sort_in_place(arr: List[T], low: int = 0, high: int | None = None) -> List[T]:
    """
    Sort a list in ascending order in place using Lomuto partitioning.

    Args:
        arr: List of comparable elements to sort.
        low: Starting index of the sub-array to sort.
        high: Ending index (inclusive) of the sub-array to sort.

    Returns:
        The same list, sorted in place.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = _partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

    return arr


def _partition(arr: List[T], low: int, high: int) -> int:
    """Lomuto partition scheme: places the pivot in its final position."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1