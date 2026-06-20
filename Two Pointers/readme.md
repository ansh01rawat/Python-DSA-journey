# Two Pointers

## Overview

This folder contains solutions to problems that use the **Two Pointers** technique.

Two Pointers is an efficient algorithmic pattern where two indices move through a data structure (usually an array or string) to reduce time complexity and avoid nested loops.

This pattern is commonly used in coding interviews and competitive programming.

---

## What I Learned

* How to use two indices to traverse an array efficiently
* How to reduce brute-force solutions from O(n²) to O(n)
* When to move the left pointer and when to move the right pointer
* How to solve problems involving sorted arrays, strings, and containers

---

## Problems Solved

### Easy

* Valid Palindrome
* Merge Sorted Array
* Two Sum II (Input Array Is Sorted)

### Medium

* Container With Most Water

---

## Two Pointers Pattern

### Opposite Direction

Used when pointers start from both ends.

Example:

```python
left = 0
right = len(nums) - 1

while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

Applications:

* Valid Palindrome
* Two Sum II
* Container With Most Water

---

### Same Direction

Used when pointers move in the same direction.

Example:

```python
slow = 0

for fast in range(len(nums)):
    if condition:
        nums[slow] = nums[fast]
        slow += 1
```

Applications:

* Remove Duplicates
* Move Zeroes

---

## Time Complexity Benefits

| Approach     | Complexity |
| ------------ | ---------- |
| Brute Force  | O(n²)      |
| Two Pointers | O(n)       |

Two Pointers often eliminates the need for nested loops, resulting in faster and more efficient solutions.

---

## Key Problems

### Valid Palindrome

Concepts:

* String traversal
* Ignoring special characters
* Comparing characters from both ends

Complexity:

* Time: O(n)
* Space: O(1)

---

### Two Sum II

Concepts:

* Sorted arrays
* Moving pointers based on current sum

Complexity:

* Time: O(n)
* Space: O(1)

---

### Merge Sorted Array

Concepts:

* Backward traversal
* In-place modification

Complexity:

* Time: O(m + n)
* Space: O(1)

---

### Container With Most Water

Concepts:

* Area calculation
* Moving the shorter wall
* Greedy reasoning

Complexity:

* Time: O(n)
* Space: O(1)

---

## Important Takeaways

* Always look for sorted arrays.
* Consider Two Pointers before using nested loops.
* Move the pointer that limits the current answer.
* Practice understanding why pointers move instead of memorizing solutions.

---

## Future Problems

* 3Sum
* Trapping Rain Water
* Boats to Save People
* Remove Duplicates from Sorted Array
* Move Zeroes

---

### Author

Ansh Rawat

B.Tech CSE (Applied Mathematics)

Python DSA Journey
