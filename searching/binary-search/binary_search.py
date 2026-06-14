def binary_search (arr, target):
    """
    Search for a target value in a sorted array using
    the Binary Search algorithm.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Returns:
        Index of target if found, otherwise -1.
    """

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
