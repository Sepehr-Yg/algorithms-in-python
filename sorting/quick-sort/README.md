# Quick Sort

A divide-and-conquer sorting algorithm: pick a pivot, partition the rest
of the list around it, and recursively sort the partitions.

## How It Works

1. Choose a **pivot** (this implementation uses the middle element, to
   reduce the chance of worst-case behavior on sorted input).
2. **Partition** the remaining elements into: less than, equal to, and
   greater than the pivot.
3. Recursively sort the "less than" and "greater than" groups.
4. Combine: `sorted(less) + equal + sorted(greater)`.

This repo includes two versions:
- `quick_sort()` — simple, readable, uses extra memory.
- `quick_sort_in_place()` — in-place with Lomuto partitioning, the
  version usually expected in technical interviews.

**Example:** `[10, 7, 8, 9, 1, 5]`, pivot `9` → less=`[7,8,1,5]`,
equal=`[9]`, greater=`[10]`. Recursing on each side eventually gives
`[1, 5, 7, 8, 9, 10]`.

## Usage

```python
from quick_sort import quick_sort, quick_sort_in_place

data = [10, 7, 8, 9, 1, 5]
print(quick_sort(data))                  # [1, 5, 7, 8, 9, 10]
print(quick_sort_in_place(data.copy()))  # [1, 5, 7, 8, 9, 10]
```

## Complexity

| Case    | Time       | Space    |
|---------|------------|----------|
| Best    | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst   | O(n²)      | O(n)     |

Not stable. Worst case happens when the pivot is repeatedly the smallest
or largest element — picking the middle element (as done here) makes this
unlikely in practice.

## When to Use It

Usually the fastest general-purpose in-memory sort in practice, and the
basis for sort implementations in many languages' standard libraries.

## Running the Example

```bash
python example.py
```

## Related

- Article link: coming soon
- Part of the [algorithms-in-python](https://github.com/Sepehr-Yg/algorithms-in-python) repository.