# Merge Sort

A divide-and-conquer sorting algorithm: split the list into halves, sort
each half recursively, then merge the sorted halves back together.

## How It Works

1. **Divide:** Split the list into two halves.
2. **Conquer:** Recursively sort each half (a list of 0 or 1 elements is
   already sorted).
3. **Combine:** Merge the two sorted halves by repeatedly comparing their
   front elements and taking the smaller one.

**Example:** `[38, 27, 43, 3, 9, 82, 10]` splits down to single elements,
then merges back up: `[27,38] + [3,43] → [3,27,38,43]`, `[9,82] + [10] →
[9,10,82]`, and finally `[3,27,38,43] + [9,10,82] → [3,9,10,27,38,43,82]`.

## Usage

```python
from merge_sort import merge_sort

data = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(data))  # [3, 9, 10, 27, 38, 43, 82]
```

Note: this returns a **new** sorted list rather than sorting in place —
that's the standard way to implement merge sort.

## Complexity

| Case    | Time       | Space |
|---------|------------|-------|
| Best    | O(n log n) | O(n)  |
| Average | O(n log n) | O(n)  |
| Worst   | O(n log n) | O(n)  |

Stable — equal elements keep their relative order. Guaranteed O(n log n)
in every case, at the cost of O(n) extra memory for merging.

## When to Use It

Good when you need guaranteed O(n log n) performance regardless of input
order — e.g., sorting linked lists or data too large to fit in memory.

## Running the Example

```bash
python example.py
```

## Related

- Article link: coming soon
- Part of the [algorithms-in-python](https://github.com/Sepehr-Yg/algorithms-in-python) repository.