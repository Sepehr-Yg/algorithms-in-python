# Insertion Sort

An in-place sorting algorithm that builds the sorted list one element at
a time, the same way you'd sort a hand of playing cards.

## How It Works

1. Treat the first element as a sorted list of size 1.
2. Take the next element (the "key") and compare it to the elements before it.
3. Shift every element greater than the key one position to the right.
4. Insert the key into the gap that was created.
5. Repeat for every element.

**Example:** `[12, 11, 13, 5, 6]` → `[5, 6, 11, 12, 13]`
`11` gets inserted before `12`, `13` stays put, `5` moves to the front, `6` slots in after `5`.

## Usage

```python
from insertion_sort import insertion_sort

data = [12, 11, 13, 5, 6]
print(insertion_sort(data))  # [5, 6, 11, 12, 13]
```

## Complexity

| Case    | Time  | Space |
|---------|-------|-------|
| Best    | O(n)  | O(1)  |
| Average | O(n²) | O(1)  |
| Worst   | O(n²) | O(1)  |

Stable — equal elements keep their relative order. The best case (O(n))
happens on already-sorted input, since the inner loop never runs.

## When to Use It

Efficient for small or nearly-sorted datasets. Python's own `sorted()`
(Timsort) actually falls back to insertion sort for small sub-arrays.

## Running the Example

```bash
python example.py
```

## Related

- Article link: coming soon
- Part of the [algorithms-in-python](https://github.com/Sepehr-Yg/algorithms-in-python) repository.