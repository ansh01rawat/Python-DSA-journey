# 📊 Graphs — Python DSA Journey

This folder contains my practice and implementations of **Graph and Grid traversal algorithms** in Python.

The goal of this section is to build a strong understanding of **DFS, BFS, graph representation, connected components, shortest paths, and grid-based graph problems**.

---

## 🧠 Topics Covered

* Graph Representation
* Depth First Search (DFS)
* Breadth First Search (BFS)
* Grid Traversal
* Connected Components
* Flood Fill
* Multi-Source BFS
* Shortest Path in Unweighted Graphs
* State-Space BFS
* Visited Sets and Graph Traversal
* Matrix/Grid Graph Problems

---

## 📁 Problems & Implementations

| File                      | Concept                              |
| ------------------------- | ------------------------------------ |
| `Graph representation.py` | Graph representation basics          |
| `Depth First Search.py`   | DFS traversal                        |
| `Breadth First Search.py` | BFS traversal                        |
| `Number of Provinces.py`  | DFS / Connected Components           |
| `Number of Islands.py`    | Grid DFS / Connected Components      |
| `Flood Fill.py`           | DFS Grid Traversal                   |
| `Rotting Oranges.py`      | Multi-Source BFS                     |
| `01 Matrix.py`            | Multi-Source BFS + Shortest Distance |
| `Open The Lock.py`        | BFS on State Graph                   |
| `Word Ladder.py`          | BFS + Word/State Graph               |

---

## 🔥 Key Patterns Learned

### 1. Depth First Search

DFS is useful when we need to completely explore a connected region before moving elsewhere.

Common applications:

* Connected components
* Number of Islands
* Flood Fill
* Graph traversal

---

### 2. Breadth First Search

BFS explores a graph **level by level**.

This makes it especially useful for finding the **shortest path in an unweighted graph**.

```text
Start
 ↓
Distance 1
 ↓
Distance 2
 ↓
Distance 3
```

---

### 3. Multi-Source BFS

Instead of starting BFS from one cell, we can start from **multiple cells simultaneously**.

Used in:

* `Rotting Oranges.py`
* `01 Matrix.py`

General pattern:

```text
Multiple starting points
        ↓
      Queue
        ↓
       BFS
        ↓
Minimum distance / time
```

---

### 4. BFS on State Graphs

Graphs don't always look like:

```text
(row, col)
```

A graph node can also be a **state**.

Examples:

```text
Open The Lock → "0000"
Word Ladder   → "hit"
```

The important idea is:

> If each move has the same cost and we need the minimum number of moves, BFS is usually a strong candidate.

---

## 🧩 Important LeetCode Problems

### 🟢 Number of Provinces

**Concept:** Connected Components + DFS

Finds the number of separate groups of connected cities.

---

### 🟢 Number of Islands

**Concept:** Grid DFS

Treats every land cell as a graph node and explores each connected island.

---

### 🟢 Flood Fill

**Concept:** DFS + Grid Traversal

Explores connected cells having the same original color and changes them to the target color.

---

### 🟡 Rotting Oranges

**Concept:** Multi-Source BFS

Starts BFS from all rotten oranges simultaneously and calculates the minimum time required to rot all reachable fresh oranges.

---

### 🟡 01 Matrix

**Concept:** Multi-Source BFS + Shortest Distance

Starts BFS from every `0` and calculates the shortest distance from every cell to the nearest `0`.

---

### 🟡 Open The Lock

**Concept:** BFS + State Graph

Treats every four-digit lock combination as a graph state and finds the minimum number of turns required to reach the target.

---

### 🟡 Word Ladder

**Concept:** BFS + State Graph

Treats words as graph nodes and finds the shortest transformation sequence between two words.

---

## 💡 Core DSA Patterns

### DFS

```text
Visit node
   ↓
Mark visited
   ↓
Visit neighbours
   ↓
Repeat
```

### BFS

```text
Add starting node
      ↓
    Queue
      ↓
Pop node
      ↓
Generate neighbours
      ↓
Add unvisited neighbours
      ↓
Repeat
```

### Shortest Path

```text
Unweighted graph
       +
Equal movement cost
       ↓
      BFS
```

---

## 📈 Learning Progress

Current progression:

```text
Graph Representation
        ↓
       DFS
        ↓
       BFS
        ↓
Connected Components
        ↓
Grid Traversal
        ↓
Multi-Source BFS
        ↓
Shortest Path BFS
        ↓
State-Space BFS
```

---

## 🛠️ Language & Tools

* **Language:** Python
* **Practice Platform:** LeetCode
* **Repository:** Python-DSA-Journey

---

## 🎯 Goal

Build a strong foundation in graph algorithms and develop the ability to recognize common graph patterns while solving DSA problems.

> **Learn the pattern, understand the reasoning, then implement the solution.**

---

### 🚀 Next Topics

Planned graph topics include:

* Pacific Atlantic Water Flow
* Graph Cycle Detection
* Topological Sort
* Course Schedule
* Union Find / Disjoint Set Union
* Dijkstra's Algorithm
* Minimum Spanning Tree
* Advanced Graph Problems
