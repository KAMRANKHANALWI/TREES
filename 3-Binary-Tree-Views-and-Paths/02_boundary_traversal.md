# Boundary Traversal of Binary Tree

## 1. Problem

Given the root of a binary tree, return its **boundary nodes in anti-clockwise order**, starting from the root.

**The boundary consists of:**

1. Root
2. Left boundary (excluding leaves)
3. Leaf nodes (left to right)
4. Right boundary (excluding leaves, bottom to top)

## 2. Key Observation

$$
\color{#1f6feb}{\text{Boundary = Root + Left Boundary + Leaves + Reversed Right Boundary}}
$$

Split the problem into three independent helpers and join their results in order.

Leaves are excluded from the two side walks because the leaf pass already collects them. This avoids duplicates.

## 3. Core Logic

| Part | Traversal Rule | Order in answer |
|---|---|---|
| Root | Add once (skip if it is a leaf) | First |
| Left boundary | Go down, prefer left, fallback right | Top → bottom |
| Leaf nodes | DFS, left before right | Left → right |
| Right boundary | Go down, prefer right, fallback left | Collect top → bottom, then **reverse** |

### Leaf Condition

```python
def is_leaf(node):
    return node.left is None and node.right is None
```

A node with even one child is not a leaf.

### Helper Functions

**1. Left Boundary**

```python
node = root.left

while node:
    if is_leaf(node):
        break

    ans.append(node.val)
    node = node.left if node.left else node.right
```

**2. Leaf Nodes**

```python
def add_leaves(node, ans):
    if node is None:
        return

    if is_leaf(node):
        ans.append(node.val)
        return

    add_leaves(node.left, ans)
    add_leaves(node.right, ans)
```

**3. Right Boundary**

```python
node = root.right
temp = []

while node:
    if is_leaf(node):
        break

    temp.append(node.val)
    node = node.right if node.right else node.left

ans.extend(temp[::-1])
```

### Full Solution

```python
def boundary_traversal(root):
    if root is None:
        return []

    ans = []

    if not is_leaf(root):
        ans.append(root.val)

    # left boundary
    node = root.left
    while node:
        if is_leaf(node):
            break
        ans.append(node.val)
        node = node.left if node.left else node.right

    # leaves
    add_leaves(root, ans)

    # right boundary
    node = root.right
    temp = []
    while node:
        if is_leaf(node):
            break
        temp.append(node.val)
        node = node.right if node.right else node.left
    ans.extend(temp[::-1])

    return ans
```

### Edge Case

If the root itself is a leaf (single node), it must be added only once. The `if not is_leaf(root)` guard handles this, since `add_leaves` already adds it.

## 4. Example

```text
          1
        /   \
       2     3
      / \     \
     4   5     6
        / \     \
       8   9     7
```

| Step | Nodes added | Answer so far |
|---|---|---|
| Root | `1` | `[1]` |
| Left boundary | `2` (stops at `4`, a leaf) | `[1, 2]` |
| Leaves | `4, 8, 9, 7` | `[1, 2, 4, 8, 9, 7]` |
| Right boundary | `3, 6` collected, reversed to `6, 3` (stops at `7`, a leaf) | `[1, 2, 4, 8, 9, 7, 6, 3]` |

**Final output:**

```python
[1, 2, 4, 8, 9, 7, 6, 3]
```

## 5. Complexity

Let $N$ = number of nodes and $H$ = tree height.

| Complexity | Value |
|---|---|
| Time | $O(N)$ |
| Auxiliary space | $O(H)$ |
| Output space | $O(N)$ |