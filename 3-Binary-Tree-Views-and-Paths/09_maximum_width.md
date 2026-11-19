## Maximum Width of Binary Tree

The width of a binary tree is the maximum number of positions between the leftmost and rightmost non-null nodes at any level, including empty positions in between.

To calculate this, we use **Level Order Traversal (BFS)** and assign every node a position as if the tree were a complete binary tree.

For a node at index $i$:

- Left child: $\color{#1f6feb}{2i+1}$
- Right child: $\color{#1f6feb}{2i+2}$

At each level, the width is determined by:

$$
\color{#1f6feb}{Width = Rightmost\ Index - Leftmost\ Index + 1}
$$

**Example:**

```text
              1(0)
            /      \
         2(1)      3(2)
         /            \
       4(3)           5(6)
```

Although the last level contains only two actual nodes, its width is $6-3+1=\color{#1f6feb}{4}$, because the empty positions between them are also counted.

**Index Normalization**

In a deep tree, positional indexes can become very large. To avoid this, subtract the first index of each level from every index at that level.

For example:

```text
Original:      [100, 101, 104, 106]
Normalized:    [  0,   1,   4,   6]
```

The relative gaps remain unchanged, so the width stays the same.

**Core Logic:**

```python
first_index = queue[0][1]
index -= first_index

width = last - first + 1
max_width = max(max_width, width)
```

| Complexity      | Value    |
| --------------- | -------- |
| Time            | $O(N)$ |
| Auxiliary Space | $O(N)$ |

**Key Takeaway:** $\color{#1f6feb}{BFS + Positional\ Indexing}$ helps calculate width accurately, even when empty positions exist between nodes. Normalization keeps indexes manageable.