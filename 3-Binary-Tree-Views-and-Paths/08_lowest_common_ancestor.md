# Lowest Common Ancestor (LCA) of Binary Tree

## 1. Understanding the Problem

Given two nodes `p` and `q` in a binary tree, find their Lowest Common Ancestor.

The Lowest Common Ancestor is the **deepest node that is an ancestor of both target nodes**. A node can also be an ancestor of itself.

Consider:

```text
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
```

If our targets are `4` and `5`, their paths meet at node `2`.

Therefore:

```python
LCA(4, 5) = 2
```

If our targets are `4` and `6`, their paths meet at node `1`.

```python
LCA(4, 6) = 1
```

## 2. The Key Observation: DFS + Information Propagation

Instead of storing both root-to-node paths and comparing them, we can solve this problem using a single recursive DFS.

Think about what we need to know at every node:

- Does its left subtree contain either target?
- Does its right subtree contain either target?

Our recursive function returns a `TreeNode` reference or `None`.

When a target is found, we return that node. As this information travels back up the recursion, each parent checks the results from its left and right subtrees.

$$
\color{#1f6feb}{\text{LCA = First Node Where Both Subtrees Return Non-None}}
$$

## 3. Understanding the Recursive Cases

First, handle an empty subtree:

```python
if root is None:
    return None
```

If the current node itself is one of the targets, return it:

```python
if root is p or root is q:
    return root
```

This is important because a node can be an ancestor of itself.

Now search both subtrees:

```python
left = lowest_common_ancestor(root.left, p, q)
right = lowest_common_ancestor(root.right, p, q)
```

There are two important situations.

**Case 1: Both sides return a node**

```python
if left and right:
    return root
```

One target has been found in the left subtree and the other in the right subtree. The current node is their LCA.

**Case 2: Only one side returns a node**

```python
if left:
    return left

return right
```

We simply pass the non-None result upwards. The LCA may already have been found deeper in that subtree.

## 4. How Recursive Results Travel Upwards

Find the LCA of nodes `4` and `5`:

```text
             1
           /   \
          2     3
         / \
        4   5
```

At node `2`:

```python
left = TreeNode(4)
right = TreeNode(5)
```

Both results exist, so node `2` returns itself.

At node `1`:

```python
left = TreeNode(2)
right = None
```

Only the left side returned a result, so node `1` propagates node `2` upwards.

The final answer is:

```python
2
```

This is the beauty of the recursive approach: we don't need to store complete paths. Each subtree simply reports what it found.

## 5. Complete Solution

```python
def lowest_common_ancestor(root, p, q):

    # Empty subtree
    if root is None:
        return None

    # Current node is one of the targets
    if root is p or root is q:
        return root

    # Search both subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # Targets found in opposite subtrees
    if left and right:
        return root

    # Propagate the non-None result
    if left:
        return left

    return right
```

Here, `p` and `q` are TreeNode references, so we use `is` to compare node identity rather than comparing their values.

## 6. Complexity Analysis

Let \(N\) be the number of nodes and \(H\) be the height of the tree.

| Complexity | Value |
|---|---|
| Time | \(O(N)\) |
| Auxiliary space | \(O(H)\) |

Every node is visited at most once, and the recursion stack can grow up to the height of the tree.

## 7. Final Takeaway

The key to this problem is understanding what each recursive call returns.

- `None` means neither target was found in that subtree.
- A target node means that target was found.
- Two non-None results mean the current node is the LCA.
- One non-None result is propagated upwards.

$$
\color{#1f6feb}{\text{DFS + Recursive Returns + Information Propagation}}
$$

Instead of finding two separate paths, we let the recursive calls carry information upwards until the Lowest Common Ancestor is identified.