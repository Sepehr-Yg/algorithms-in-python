def bubble_sort(a):
    """
    Sort a list using the Bubble Sort algorithm.

    Time Complexity:
        Worst Case: O(n²)
        Average Case: O(n²)
        Best Case: O(n)

    Space Complexity:
        O(1)

    Returns:
        Sorted list
    """

    n = len(a)

    for p in range(n - 1):
        swapped = False
        
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        
        if not swapped:
            break

    return a