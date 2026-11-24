# Count Nodes in a Complete Binary Tree

## 1. Understanding the Problem

Given the root of a **Complete Binary Tree**, count the total number of nodes present in it.

A Complete Binary Tree is a binary tree in which:

- Every level is completely filled, except possibly the last level.
- The last level must be filled from **left to right**, without gaps.

### Example 1: Complete Binary Tree

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

This tree is complete because the last level is filled from left to right.

Total nodes = `6`.

### Example 2: Not a Complete Binary Tree

```text
          1
        /   \
       2     3
        \
         5
```

This tree is not complete because node `2` has a right child but no left child.

Our goal is to count all nodes efficiently.

---

## 2. Basic Approach: Recursive Counting

The simplest way to count nodes is to recursively count the left and right subtrees.

For every node:

1. Count the nodes in its left subtree.
2. Count the nodes in its right subtree.
3. Add `1` for the current node.

```python
def count_nodes(root):
    if root is None:
        return 0

    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)

    return 1 + left_count + right_count
```

The logic is:

$$
\text{Total Nodes} = 1 + L + R
$$

Where:

- `1` represents the current node.
- `L` represents the number of nodes in the left subtree.
- `R` represents the number of nodes in the right subtree.

This approach visits every node exactly once.

**Complexity:**

- Time: $O(N)$
- Space: $O(H)$ for recursion stack.

Although this works, it does not take advantage of the special structure of a Complete Binary Tree.

We can optimize it.

---

## 3. Key Observation: Perfect Binary Tree

A **Perfect Binary Tree** is a tree in which every level is completely filled.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Notice that if we know the height of a perfect binary tree, we can calculate its total number of nodes directly.

For a perfect binary tree:

$$
\text{Total Nodes} = 2^H - 1
$$

Where `H` is the height measured in number of levels.

For example, if the height is `3`:

$$
2^3 - 1 = 8 - 1 = 7
$$

We do not need to visit all seven nodes individually.

**Key observation:**

\color{#1f6feb}{If the leftmost height and rightmost height of a Complete Binary Tree subtree are equal, that subtree is perfect.}

Therefore, we can calculate its node count directly.

This is the main optimization.

---

## 4. Calculating Leftmost and Rightmost Heights

To check whether a subtree is perfect, we calculate two heights.

### Leftmost Height

Start from the current node and keep moving only towards the left child.

```python
def left_height(node):
    height = 0

    while node:
        height += 1
        node = node.left

    return height
```

### Rightmost Height

Start from the current node and keep moving only towards the right child.

```python
def right_height(node):
    height = 0

    while node:
        height += 1
        node = node.right

    return height
```

Consider this tree:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Starting from root `1`:

- Leftmost path: `1 → 2 → 4`
- Rightmost path: `1 → 3 → 7`

Therefore:

$$
LH = 3,\quad RH = 3
$$

Since both heights are equal, the subtree is perfect.

Its node count is:

$$
2^3 - 1 = 7
$$

### Important Condition

Equal leftmost and rightmost heights indicate a perfect subtree **because the original tree is guaranteed to be complete**.

For an arbitrary binary tree, equal heights do not necessarily mean that the tree is perfect.

---

## 5. Optimized Recursive Approach

Now we combine the height calculation with recursion.

For every subtree, there are two possible cases.

### Case 1: Leftmost Height Equals Rightmost Height

```python
if lh == rh:
    return (1 << lh) - 1
```

The subtree is perfect, so we calculate its node count directly.

The expression:

```python
(1 << lh) - 1
```

is equivalent to:

```python
(2 ** lh) - 1
```

The bit-shift operation is used here to calculate the power of two.

### Case 2: Leftmost Height Does Not Equal Rightmost Height

```python
return 1 + count_nodes(root.left) + count_nodes(root.right)
```

The subtree is complete but not perfect.

Therefore, we recursively count:

1. The current node.
2. All nodes in the left subtree.
3. All nodes in the right subtree.

The recursive formula remains:

$$
N = 1 + L + R
$$

The important difference is that perfect subtrees are counted directly instead of visiting every node.

---

## 6. Complete Dry Run

Consider the following complete binary tree:

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

Expected answer: `6`.

### Step 1: Start from Root (1)

Calculate the leftmost and rightmost heights.

Leftmost path:

```text
1 → 2 → 4
```

Rightmost path:

```text
1 → 3
```

Therefore:

$$
LH = 3,\quad RH = 2
$$

Since:

$$
LH \neq RH
$$

The tree is not perfect.

We recursively count its left and right subtrees.

### Step 2: Process Left Subtree (2)

```text
       2
      / \
     4   5
```

Leftmost path: `2 → 4`

Rightmost path: `2 → 5`

Therefore:

$$
LH = 2,\quad RH = 2
$$

Both heights are equal.

This subtree is perfect, so:

$$
2^2 - 1 = 3
$$

We return `3` directly.

Notice that we did not recursively visit nodes `4` and `5`.

### Step 3: Process Right Subtree (3)

```text
       3
      /
     6
```

Leftmost path: `3 → 6`

Rightmost path: `3`

Therefore:

$$
LH = 2,\quad RH = 1
$$

The heights are different, so we recursively count its children.

- Node `6` is a leaf, so its count is `1`.
- The right child is `None`, so its count is `0`.

Therefore:

$$
1 + 1 + 0 = 2
$$

The right subtree contains `2` nodes.

### Step 4: Return to Root (1)

Now we have:

- Current root: `1`
- Left subtree count: `3`
- Right subtree count: `2`

Therefore:

$$
N = 1 + 3 + 2
$$

$$
\boxed{N = 6}
$$

Final answer: `6`.

---

## 7. Complete Python Solution

```python
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Calculate the leftmost height
def left_height(node):
    height = 0

    while node:
        height += 1
        node = node.left

    return height


# Calculate the rightmost height
def right_height(node):
    height = 0

    while node:
        height += 1
        node = node.right

    return height


# Optimized count of nodes in a complete binary tree
def count_nodes(root):
    if root is None:
        return 0

    lh = left_height(root)
    rh = right_height(root)

    # Perfect subtree: calculate directly
    if lh == rh:
        return (1 << lh) - 1

    # Otherwise, recursively count both subtrees
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    print("Total Nodes:", count_nodes(root))
```

**Output:**

```text
Total Nodes: 6
```

---

## 8. Complexity Analysis

Let `N` be the total number of nodes and `H` be the height of the tree.

### Time Complexity: $O(\log^2 N)$

A Complete Binary Tree has height:

$$
H = O(\log N)
$$

At each recursive call:

- Calculating the leftmost height takes $O(\log N)$.
- Calculating the rightmost height takes $O(\log N)$.

So, height calculation takes:

$$
O(\log N)
$$

If both heights are equal, we return immediately.

Otherwise, we recursively process the two subtrees. Because the tree is complete, at least one of these subtrees is perfect and gets counted directly. Only the other subtree needs further recursion.

Thus, there are at most $O(\log N)$ recursive levels, with $O(\log N)$ work per level.

Therefore:

$$
\boxed{O(\log^2 N)}
$$

### Space Complexity: $O(\log N)$

The algorithm uses recursion.

The maximum recursion depth is proportional to the height of the tree.

Since:

$$
H = O(\log N)
$$

Space complexity is:

$$
\boxed{O(\log N)}
$$

---

## 9. Edge Cases

| Input                      | Expected Output | Reason                             |
| -------------------------- | --------------: | ---------------------------------- |
| Empty tree                 |               0 | No nodes                           |
| Single node                |               1 | One root node                      |
| Perfect tree of height 3   |               7 | $2^3 - 1$                          |
| Complete tree with 5 nodes |               5 | Last level is partially filled     |
| Complete tree with 6 nodes |               6 | Last level is filled left to right |

---

## 10. Final Takeaway

The basic recursive approach counts every node individually and takes $O(N)$ time.

The optimized approach uses the special structure of a Complete Binary Tree.

The most important observation is:

$\color{#1f6feb}{\text{If the leftmost height equals the rightmost height, the subtree is perfect and its node count is } 2^H - 1}$

Otherwise, recursively count its left and right subtrees.

Remember these three things:

1. A complete binary tree has all levels filled except possibly the last, which is filled from left to right.
2. Equal leftmost and rightmost heights indicate a perfect subtree under the complete-tree guarantee.
3. The optimized approach reduces the time complexity from $O(N)$ to $O(\log^2 N)$.

**Pattern:** Binary Tree Recursion + Height Calculation + Complete Binary Tree Properties.
