# 🧩 LeetCode Submissions

Personal repository tracking my LeetCode solutions and progress through the [NeetCode 150](https://neetcode.io/practice) curriculum. Solutions are written in **Python**, with a focus on pattern recognition and understanding over raw problem count.

---

## 📌 Approach

I use **Anki spaced repetition** alongside active problem-solving to consolidate pattern knowledge. Rather than optimising for volume, the goal is:

- Identifying the underlying **pattern and signals** before writing any code
- Being able to **reconstruct** solutions from first principles, not memorisation
- Building cold-solve ability on unseen problems through timed mixed practice

---

## 📂 Structure

```
leetcode/
├── arrays_hashing/
├── two_pointers/
├── sliding_window/
├── stack/
├── binary_search/
├── linked_list/
├── trees/
├── tries/
├── backtracking/
├── heap_priority_queue/
├── intervals/
├── greedy/
├── graphs/
├── advanced_graphs/
├── dynamic_programming/
│   ├── 1d/
│   └── 2d/
├── bit_manipulation/
└── math_geometry/
```

Each folder contains solutions named by LeetCode problem number and title, e.g. `0001_two_sum.py`.

---

## ✅ Progress

Tracking against the NeetCode 150. Problems marked ✅ are solved and consolidated in Anki.

| Topic | Progress | Notes |
|---|---|---|
| Arrays & Hashing | 🟢 In progress | |
| Two Pointers | 🟢 In progress | |
| Sliding Window | 🟢 In progress | |
| Stack | 🟢 In progress | |
| Binary Search | 🟢 In progress | |
| Linked List | 🟢 In progress | |
| Trees | 🟢 In progress | |
| Tries | 🟡 Partial | |
| Backtracking | 🟡 Partial | |
| Heap / Priority Queue | 🔴 Not started | Next focus area |
| Intervals | 🟡 Partial | |
| Greedy | 🔴 Not started | |
| Graphs | 🔴 Not started | |
| Advanced Graphs | 🔴 Not started | |
| 1D Dynamic Programming | 🔴 Not started | |
| 2D Dynamic Programming | 🔴 Not started | |
| Bit Manipulation | 🟡 Partial | |
| Math & Geometry | 🟡 Partial | |

---

## 🧠 Solution Format

Each solution file includes:

```python
# Problem: Two Sum (LeetCode #1)
# Difficulty: Easy
# Pattern: Hash Map / Complement lookup
# Time: O(n) | Space: O(n)

# --- Approach ---
# Iterate through nums, storing each value's index in a hash map.
# For each element, check if its complement (target - num) already exists.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

---

## 🔑 Pattern Reference

A quick index of core patterns and their typical signals:

| Signal | Pattern |
|---|---|
| Sorted array, find pair/target | Two Pointers |
| Subarray/substring with constraint | Sliding Window |
| Nested brackets, LIFO order | Stack |
| Sorted array, find element | Binary Search |
| Frequency count, grouping | Hash Map |
| Shortest path, level-by-level | BFS |
| Explore all paths, connected components | DFS |
| k-th largest/smallest, streaming | Heap |
| Make locally optimal choices | Greedy |
| Overlapping subproblems, optimal substructure | Dynamic Programming |
| All combinations/permutations | Backtracking |

---

## 📈 Stats

- **Total solved:** ~50
- **NeetCode 150 coverage:** ~75% of topics touched (missing heaps, graphs, DP, greedy)
- **Language:** Python 3

---

*This repo is part of my broader preparation for junior/graduate software engineering roles alongside portfolio projects in Java/Spring Boot and React.*
