"""
Example usage and sanity checks for quick_sort() and quick_sort_in_place().
Run directly to verify the implementation: python example.py
"""

from quick_sort import quick_sort, quick_sort_in_place

if __name__ == "__main__":
    cases = [
        [10, 7, 8, 9, 1, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [42],
        [3, 1, 3, 2, 1],
        [-5, 3, -1, 0, 2],
        ["banana", "apple", "cherry"],
    ]

    for case in cases:
        original = case.copy()

        result_functional = quick_sort(case)
        assert result_functional == sorted(original), f"Failed on input: {original}"

        result_in_place = quick_sort_in_place(case.copy())
        assert result_in_place == sorted(original), f"Failed on input: {original}"

        print(f"{original} -> {result_functional}")

    print("\nAll checks passed.")