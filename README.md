# ð§© LeetCode Submissions

Personal repository tracking my LeetCode solutions and progress through the [NeetCode 150](https://neetcode.io/practice) curriculum. Solutions are written in **Python**, with a focus on pattern recognition and understanding over raw problem count.

---

## ð Approach

I use **Anki spaced repetition** alongside active problem-solving to consolidate pattern knowledge. Rather than optimising for volume, the goal is:

- Identifying the underlying **pattern and signals** before writing any code
- Being able to **reconstruct** solutions from first principles, not memorisation
- Building cold-solve ability on unseen problems through timed mixed practice

---

## ð Structure

```
leetcode/
âââ arrays_hashing/
âââ two_pointers/
âââ sliding_window/
âââ stack/
âââ binary_search/
âââ linked_list/
âââ trees/
âââ tries/
âââ backtracking/
âââ heap_priority_queue/
âââ intervals/
âââ greedy/
âââ graphs/
âââ advanced_graphs/
âââ dynamic_programming/
â   âââ 1d/
â   âââ 2d/
âââ bit_manipulation/
âââ math_geometry/
```

Each folder contains solutions named by LeetCode problem number and title, e.g. `0001_two_sum.py`.

---

## â Progress

Tracking against the NeetCode 150. Problems marked â are solved and consolidated in Anki.

| Topic | Progress | Notes |
|---|---|---|
| Arrays & Hashing | ð¢ In progress | |
| Two Pointers | ð¢ In progress | |
| Sliding Window | ð¢ In progress | |
| Stack | ð¢ In progress | |
| Binary Search | ð¢ In progress | |
| Linked List | ð¢ In progress | |
| Trees | ð¢ In progress | |
| Tries | ð¡ Partial | |
| Backtracking | ð¡ Partial | |
| Heap / Priority Queue | ð´ Not started | Next focus area |
| Intervals | ð¡ Partial | |
| Greedy | ð´ Not started | |
| Graphs | ð´ Not started | |
| Advanced Graphs | ð´ Not started | |
| 1D Dynamic Programming | ð´ Not started | |
| 2D Dynamic Programming | ð´ Not started | |
| Bit Manipulation | ð¡ Partial | |
| Math & Geometry | ð¡ Partial | |

---

## ð§  Solution Format

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

## ð Pattern Reference

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

## ð Stats

- **Total solved:** ~50
- **NeetCode 150 coverage:** ~75% of topics touched (missing heaps, graphs, DP, greedy)
- **Language:** Python 3

---

*This repo is part of my broader preparation for junior/graduate software engineering roles alongside portfolio projects in Java/Spring Boot and React.*

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Hash Table
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Divide and Conquer
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Sorting
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Heap (Priority Queue)
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Counting
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/dylbobuloid/Leetcode-Submissions/tree/master/0347-top-k-frequent-elements) |
<!---LeetCode Topics End-->