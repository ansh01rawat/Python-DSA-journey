# 🔄 Backtracking

Backtracking is a recursive problem-solving technique that explores all possible choices while undoing previous decisions to search for valid solutions efficiently.

---

## 📚 Problems Solved

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 78 | Subsets | Medium | ✅ |
| 90 | Subsets II | Medium | ✅ |
| 39 | Combination Sum | Medium | ✅ |
| 40 | Combination Sum II | Medium | ✅ |
| 46 | Permutations | Medium | ✅ |
| 47 | Permutations II | Medium | ✅ |
| 17 | Letter Combinations of a Phone Number | Medium | ⬜ |
| 79 | Word Search | Medium | ⬜ |
| 131 | Palindrome Partitioning | Medium | ⬜ |
| 51 | N-Queens | Hard | ⬜ |

---

## 🧠 Concepts Learned

- Recursive Depth First Search (DFS)
- Include / Exclude recursion pattern
- Recursion call stack
- Backtracking using `append()` and `pop()`
- Base case handling
- Why `subset.copy()` is required
- Handling duplicate elements
- Sorting before recursion
- Skipping duplicates only in the exclude branch

---

## 📝 Backtracking Template

```python
def dfs(index):

    if base_case:
        save_answer()
        return

    # Choose
    ...

    dfs(next_state)

    # Undo choice
    ...

    # Explore another choice
    dfs(next_state)
```

---

## ⏱️ Complexity

Most backtracking problems explore every possible combination.

- **Time Complexity:** Usually `O(2^n)` or higher depending on the problem.
- **Space Complexity:** `O(n)` recursion stack (excluding output).

---

## 🎯 Goal

Master the fundamental backtracking patterns before moving on to advanced recursive search problems.

Current Progress:

- ✅ 78. Subsets
- ✅ 90. Subsets II
- ✅ 39. Combination Sum I
- ✅ 40. Combination Sum II
- ✅ 46. Permutations
- ✅ 47. permjutations II
- ⬜ Remaining Problems

---

> Learning Focus: Understand the recursion flow and decision tree instead of memorizing solutions.
