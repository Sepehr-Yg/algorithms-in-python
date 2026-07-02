# Algorithms in Python

A structured collection of classic algorithms and data structures,
implemented in Python with clean code, complexity analysis, and a
companion Medium article for each topic.

Each algorithm lives in its own folder with:
- The algorithm implementation (typed, documented, no dead code)
- An `example.py` file with runnable usage and sanity checks
- A dedicated `README.md` explaining how it works, its complexity,
  and when to use it

New algorithms are added on a weekly cadence — this repo is actively
maintained, not a one-time upload.

## Implemented Algorithms

### Sorting

| Algorithm | Time (avg) | Space | Stable | Article |
|-----------|------------|-------|--------|---------|
| [Bubble Sort](sorting/bubble_sort) | O(n²) | O(1) | Yes | Coming soon |
| [Selection Sort](sorting/selection_sort) | O(n²) | O(1) | No | Coming soon |
| [Insertion Sort](sorting/insertion_sort) | O(n²) | O(1) | Yes | Coming soon |
| [Merge Sort](sorting/merge_sort) | O(n log n) | O(n) | Yes | Coming soon |
| [Quick Sort](sorting/quick_sort) | O(n log n) | O(log n) | No | Coming soon |

### Searching

| Algorithm | Time (avg) | Space | Article |
|-----------|------------|-------|---------|
| [Binary Search](searching/binary_search) | O(log n) | O(1) | Coming soon |

More categories (data structures, graph algorithms) are planned — see
Roadmap below.

## Usage

Each algorithm is self-contained. To try one:

```bash
git clone https://github.com/Sepehr-Yg/algorithms-in-python.git
cd algorithms-in-python/sorting/merge-sort
python example.py
```

## Roadmap

- [ ] Stack, Queue, Hash Table (data structures)
- [ ] Graph algorithms (BFS, DFS, Dijkstra)
- [ ] Heap Sort

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.