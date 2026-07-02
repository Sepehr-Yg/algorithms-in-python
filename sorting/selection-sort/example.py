"""
Example usage and sanity checks for selection_sort().
Run directly to verify the implementation: python example.py
"""

from selection_sort import selection_sort

if __name__ == "__main__":
    cases = [
        [64, 25, 12, 22, 11],
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
        result = selection_sort(case)
        assert result == sorted(original), f"Failed on input: {original}"
        print(f"{original} -> {result}")

    print("\nAll checks passed.")