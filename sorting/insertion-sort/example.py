"""
Example usage and sanity checks for insertion_sort().
Run directly to verify the implementation: python example.py
"""

from insertion_sort import insertion_sort

if __name__ == "__main__":
    cases = [
        [12, 11, 13, 5, 6],
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
        result = insertion_sort(case)
        assert result == sorted(original), f"Failed on input: {original}"
        print(f"{original} -> {result}")

    print("\nAll checks passed.")