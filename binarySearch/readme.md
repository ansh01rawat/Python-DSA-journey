# Binary Search

## Overview

This folder contains solutions to problems based on the **Binary Search** algorithm.

Binary Search is an efficient searching technique used to find an element in a **sorted array** by repeatedly dividing the search space in half.

It is one of the most important algorithms in computer science and is widely used in coding interviews.

---

## What I Learned

* How Binary Search works
* When Binary Search can be applied
* How to efficiently search in sorted arrays
* How to reduce time complexity from **O(n)** to **O(log n)**
* Identifying Binary Search patterns in problems

---

## Prerequisites

Before applying Binary Search:

* The data structure should usually be **sorted**.
* The search space should be reducible by half in each iteration.

---

## Basic Binary Search Template

```python
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

---

## Problems Solved

### Easy

* Binary Search (LeetCode 704)
* Guess Number (Leetcode 374)
* Search Insert Position (Leetcode 35)

### Medium

* *(Add future problems here)*

---

## How Binary Search Works

Example:

```python
nums = [-1, 0, 3, 5, 9, 12]
target = 9
```

### Iteration 1

```text
low = 0
high = 5
mid = 2

nums[mid] = 3
```

Since:

```text
3 < 9
```

Search in the right half:

```text
low = mid + 1
```

---

### Iteration 2

```text
low = 3
high = 5
mid = 4

nums[mid] = 9
```

Target found.

---

## Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(log n)   |
| Space Complexity | O(1)       |

---

## Why Binary Search?

### Linear Search

```text
Time Complexity: O(n)
```

Checks every element one by one.

### Binary Search

```text
Time Complexity: O(log n)
```

Eliminates half of the search space in every iteration.

Example:

```text
Array Size = 1,000,000

Linear Search → up to 1,000,000 comparisons
Binary Search → approximately 20 comparisons
```

---

## Common Binary Search Patterns

### 1. Search in Sorted Array

Example:

* Binary Search (LeetCode 704)

### 2. Search Insert Position

Find the position where an element should be inserted.

### 3. First and Last Occurrence

Find boundaries of a target element.

### 4. Search on Answer

Use Binary Search on possible answers instead of array elements.

Examples:

* Koko Eating Bananas
* Capacity To Ship Packages Within D Days

---

## Important Takeaways

* Binary Search works on sorted data.
* Always calculate:

```python
mid = low + (high - low) // 2
```

* Carefully update:

```python
low = mid + 1
high = mid - 1
```

* Watch out for off-by-one errors.

---

## Future Problems

* Search Insert Position
* First Bad Version
* Search in Rotated Sorted Array
* Find Peak Element
* Koko Eating Bananas
* Capacity To Ship Packages Within D Days

---

## Learning Outcome

Through these problems, I learned how Binary Search efficiently reduces the search space and solves searching problems in logarithmic time.

---

## Author

**Ansh Rawat**

B.Tech CSE (Applied Mathematics)

Vivekananda Institute of Professional Studies
