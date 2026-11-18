# Left and Right View of Binary Tree

## 1. Understanding the Problem

Imagine standing on the left side of a binary tree. At every level, you can see only the leftmost available node.

Similarly, if you stand on the right side, you can see the rightmost available node at every level.

Consider this tree:

```text
             1
           /   \
          2     3
         / \     \
        4   5     6
           /
          7
```

Looking from the left, we see:

```python
[1, 2, 4, 7]
```

Looking from the right, we see:

```python
[1, 3, 6, 7]
```

Notice that both views contain exactly one node from every level. The only difference is which node we select.

## 2. The Key Observation

Remember Level Order Traversal? BFS processes a binary tree one level at a time.

That means we already have everything we need.

For every level:

- The first node processed is the leftmost node.
- The last node processed is the rightmost node.

We can use the same BFS traversal for both problems.

$$
\color{#1f6feb}{\text{Left View = First Node of Every Level}}
$$

$$
\color{#1f6feb}{\text{Right View = Last Node of Every Level}}
$$

## 3. How Do We Identify the First and Last Nodes?

Before processing a level, we capture its size:

```python
level_size = len(queue)
```

This is important because the queue will receive children belonging to the next level while we process the current one.

We then process exactly `level_size` nodes.

For Left View, we select the first node:

```python
if i == 0:
    result.append(node.val)
```

For Right View, we select the last node:

```python
if i == level_size - 1:
    result.append(node.val)
```

We enqueue the left child before the right child so that BFS processes every level from left to right.

## 4. Complete Solutions

### Left View

```python
from collections import deque

def left_view(root):

    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:

        level_size = len(queue)

        for i in range(level_size):

            node = queue.popleft()

            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result
```

### Right View

```python
from collections import deque

def right_view(root):

    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:

        level_size = len(queue)

        for i in range(level_size):

            node = queue.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result
```

## 5. Example Walkthrough

Using our example tree:

```text
             1
           /   \
          2     3
         / \     \
        4   5     6
           /
          7
```

BFS processes the following levels:

| Level | Nodes in BFS order | Left View | Right View |
|---|---|---:|---:|
| 0 | `[1]` | 1 | 1 |
| 1 | `[2, 3]` | 2 | 3 |
| 2 | `[4, 5, 6]` | 4 | 6 |
| 3 | `[7]` | 7 | 7 |

**Final Outputs:**

```python
Left View:  [1, 2, 4, 7]
Right View: [1, 3, 6, 7]
```

## 6. Complexity Analysis

Let \(N\) be the total number of nodes.

| Complexity | Value |
|---|---|
| Time | \(O(N)\) |
| Auxiliary space | \(O(N)\) |
| Output space | \(O(H)\) |

Every node is visited exactly once, and one visible node is stored per level.

## 7. Final Takeaway

Both problems use the same BFS traversal. We simply change the condition used to select a node.

$$
\color{#1f6feb}{\text{BFS + Level Size + First/Last Node}}
$$

- Left View → Select `i == 0`.
- Right View → Select `i == level_size - 1`.

The important pattern is to recognise when a tree-view problem can be solved by selecting a particular node from each BFS level.