# Root to Node Path in Binary Tree

## 1. Understanding the Problem

Given the root of a binary tree and a target node, find the path from the root to that target.

For example, consider:

```text
             1
           /   \
          2     3
         / \     \
        4   5     6
           /
          7
```

If our target is `7`, the required path is:

```python
[1, 2, 5, 7]
```

We don't need every node visited during traversal. We only need the nodes that belong to the successful path.

## 2. The Key Observation: DFS + Backtracking

Think about finding node `7` manually.

We start at the root, explore the left subtree, and continue moving deeper. If a node doesn't lead to the target, we return and explore another branch.

This is exactly what DFS does.

However, we also need to remember the nodes we've visited along the current path.

We maintain a list:

```python
path = []
```

Whenever we visit a node, we add it:

```python
path.append(node.val)
```

If neither its left nor right subtree contains the target, that node doesn't belong to the successful path. We remove it:

```python
path.pop()
```

This process is called **Backtracking**.

$$
\color{#1f6feb}{\text{Backtracking = Add a node, explore, and remove it if the path fails}}
$$

## 3. How the Recursion Works

Our recursive function returns a Boolean value.

- `True` means the target has been found.
- `False` means the target was not found in that subtree.

First, handle an empty node:

```python
if node is None:
    return False
```

Then add the current node to our path:

```python
path.append(node.val)
```

Check whether we've reached the target:

```python
if node.val == target:
    return True
```

If not, search the left and right subtrees:

```python
if find_path(node.left, target, path):
    return True

if find_path(node.right, target, path):
    return True
```

If both searches fail, the current node must be removed:

```python
path.pop()
return False
```

Notice that we return immediately when either subtree finds the target. This preserves the successful path instead of removing its nodes.

## 4. Visualising Backtracking

Suppose the target is `7`.

Our search initially explores node `4`, but node `4` is not the target and has no children.

So we remove it and return to node `2`.

```text
Visit 1  → [1]
Visit 2  → [1, 2]
Visit 4  → [1, 2, 4]

Backtrack from 4:
             [1, 2]

Visit 5  → [1, 2, 5]
Visit 7  → [1, 2, 5, 7]
```

Once `7` is found, recursion returns `True` all the way back to the root.

The final path remains:

```python
[1, 2, 5, 7]
```

This is the important distinction: unsuccessful branches are removed, but the successful path is preserved.

## 5. Complete Solution

We separate the recursive DFS logic from the main function.

```python
def find_path(node, target, path):

    if node is None:
        return False

    path.append(node.val)

    if node.val == target:
        return True

    if find_path(node.left, target, path):
        return True

    if find_path(node.right, target, path):
        return True

    path.pop()

    return False


def root_to_node_path(root, target):

    path = []

    if find_path(root, target, path):
        return path

    return []
```

The wrapper function creates the path, starts the search, and returns the result. If the target doesn't exist, it returns an empty list.

## 6. Complexity Analysis

Let \(N\) be the total number of nodes and \(H\) be the height of the tree.

| Complexity      | Value    |
| --------------- | -------- |
| Time            | \(O(N)\) |
| Auxiliary space | \(O(H)\) |
| Output space    | \(O(H)\) |

In the worst case, DFS may visit every node. The recursion stack and current path can each grow up to the height of the tree.

## 7. Final Takeaway

The central idea is not just finding the target. It is maintaining the path while exploring different branches.

$$
\color{#1f6feb}{\text{DFS + Path Tracking + Backtracking}}
$$

- Append when entering a node.
- Return `True` when the target is found.
- Pop when both subtrees fail.
- Preserve the path when the target is found.
