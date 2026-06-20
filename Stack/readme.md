# Stack

## Overview

This folder contains solutions to problems based on the **Stack** data structure.

A Stack follows the **LIFO (Last In, First Out)** principle, meaning the last element added is the first one removed.

Stacks are widely used in:

* Expression evaluation
* Function calls and recursion
* Undo/Redo operations
* Browser history
* Parentheses matching
* Depth First Search (DFS)

---

## What I Learned

* How the Stack data structure works
* Push and Pop operations
* When to use a stack in problem-solving
* How stacks help solve matching and traversal problems
* Recognizing stack-based patterns in coding interviews

---

## Stack Operations

### Push

Adds an element to the top of the stack.

```python
stack = []
stack.append(10)
```

### Pop

Removes the top element.

```python
stack.pop()
```

### Peek

Views the top element without removing it.

```python
stack[-1]
```

### Check if Empty

```python
if not stack:
    print("Stack is empty")
```

---

## Problems Solved

### Easy

* Valid Parentheses

### Medium

* coming soon...

---

## Key Problem: Valid Parentheses

### Problem

Determine whether a string containing brackets is valid.

Example:

```text
Input: "()[]{}"
Output: True
```

### Concept

Use a stack to store opening brackets.

When a closing bracket appears:

* Check the top of the stack
* Verify it matches
* Remove the opening bracket

### Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(n)       |

---

## Common Stack Pattern

```python
stack = []

for item in data:

    if condition:
        stack.append(item)

    else:
        if not stack:
            return False

        stack.pop()
```

---

## Time Complexity of Operations

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |

---

## Real-Life Applications

### Browser History

```text
Visit Page A
Visit Page B
Visit Page C

Back Button → C removed first
```

### Undo Feature

```text
Type Hello
Type World

Undo → World removed first
```

### Function Calls

Python internally uses a call stack when executing functions.

---

## Important Takeaways

* Use a stack when the most recently added item must be processed first.
* Matching symbols often indicate a stack problem.
* Nested structures usually involve stacks.
* Valid Parentheses is one of the most important introductory stack problems.

---

## Future Problems

* Min Stack
* Evaluate Reverse Polish Notation
* Daily Temperatures
* Generate Parentheses
* Car Fleet
* Largest Rectangle in Histogram

---

## Learning Outcome

Through these problems, I learned how to use stacks to solve problems efficiently and identify situations where the LIFO principle is useful.

---

### Author

Ansh Rawat

B.Tech CSE (Applied Mathematics)

Python DSA Journey
