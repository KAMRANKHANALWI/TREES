# Bottom View of Binary Tree

## 1. Problem

Given the root of a binary tree, return the nodes visible when looking at the tree from the bottom, arranged from left to right.

If multiple nodes occupy the same horizontal distance, the bottommost node is selected. If nodes share the same row and column, the later node processed by BFS overwrites the earlier one.

## 2. Key Observation

Unlike Top View, where we preserve the first node encountered at each column, Bottom View keeps overwriting the value.

Since BFS processes nodes level by level, the deeper nodes are encountered later.

$$
\color{#1f6feb}{\text{Bottom View = Last BFS Node at Every Horizontal Distance}}
$$

## 3. Core Logic

The coordinate system remains the same:

- Root: column `0`
- Left child: `col - 1`
- Right child: `col + 1`

The only change is the dictionary update.

```python
# Always overwrite the existing value
bottom_view[col] = node.val
```

### Full Solution

```python
from collections import deque

def bottom_view(root):

    if root is None:
        return []

    bottom_view = {}
    queue = deque([(root, 0)])

    while queue:

        node, col = queue.popleft()

        bottom_view[col] = node.val

        if node.left:
            queue.append((node.left, col - 1))

        if node.right:
            queue.append((node.right, col + 1))

    return [bottom_view[col] for col in sorted(bottom_view)]
```

## 4. Top View vs Bottom View

| Top View | Bottom View |
|---|---|
| First node per column | Last node per column |
| Store only if column is new | Always overwrite |
| `if col not in top_view` | `bottom_view[col] = node.val` |

## 5. Example

```text
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
```

Column `0` contains nodes `1`, `5`, and `6`. Node `6` is processed last and becomes visible from below.

**Final Output:**

```python
[4, 2, 6, 3, 7]
```

## 6. Complexity

Let \(N\) be the total number of nodes.

| Complexity | Value |
|---|---|
| Time | \(O(N\log N)\) |
| Auxiliary space | \(O(N)\) |
| Output space | \(O(N)\) |

## 7. Final Takeaway

$$
\color{#1f6feb}{\text{BFS + Horizontal Distance + Overwriting}}
$$

The traversal is almost identical to Top View. The only conceptual difference is that Bottom View retains the latest encountered node at each column.