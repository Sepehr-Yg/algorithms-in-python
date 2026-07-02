"""
Example usage and sanity checks for merge_sort().
Run directly to verify the implementation: python example.py
"""

from merge_sort import merge_sort

if __name__ == "__main__":
    cases = [
        [38, 27, 43, 3, 9, 82, 10],
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
        result = merge_sort(case)
        assert result == sorted(original), f"Failed on input: {original}"
        assert case == original, "merge_sort should not mutate the input"
        print(f"{original} -> {result}")

    print("\nAll checks passed.")