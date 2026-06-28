# Linked List in Python

This folder contains implementations of various Linked List concepts and problems in Python. The goal of this section is to strengthen the understanding of pointers, node manipulation, and common linked list operations frequently asked in coding interviews.

## Topics Covered

* Creating a Node class
* Creating a Singly Linked List
* Traversal
* Insertion at a given position
* Deletion by value
* Searching for an element
* Finding the length of the linked list
* Reversing a linked list
* Merging two sorted linked lists

## Files Included

| File                        | Description                                  |
| --------------------------- | -------------------------------------------- |
| `singly_linked_list.py`     | Basic implementation of a singly linked list |
| `reverse_linked_list.py`    | Reverse a linked list using pointers         |
| `merge_two_sorted_lists.py` | Merge two sorted linked lists                |
| `search_linked_list.py`     | Search for a value in the linked list        |
| `length_linked_list.py`     | Find the length of the linked list           |

## Sample Node Structure

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

## Time Complexity

| Operation              | Time Complexity |
| ---------------------- | --------------- |
| Traversal              | O(n)            |
| Search                 | O(n)            |
| Insertion at Beginning | O(1)            |
| Insertion at End       | O(n)            |
| Deletion               | O(n)            |
| Reverse                | O(n)            |

## LeetCode Problems Solved

* LeetCode 206 - Reverse Linked List
* LeetCode 21 - Merge Two Sorted Lists
* Leetcode 83 - Remove Duplicates  From List
* Leetcode 876 - Middle Of The Linked List
* Leetcode 141 - Linked List Cycle
* Leetcode 160 - Intersection Of Two Linked List
* Leetcode 19 - Remove Nth Node From The List
## Key Learnings

* Understanding pointer manipulation
* Working with dynamic data structures
* Improving problem-solving skills
* Building a strong foundation for technical interviews

---

This folder is a part of my Python DSA Journey, where I consistently practice and document Data Structures and Algorithms concepts.
