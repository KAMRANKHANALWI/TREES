# Top View of Binary Tree

## 1. Understanding the Problem

Imagine looking at a binary tree from directly above. Some nodes will be visible, while others will be hidden behind nodes that are positioned higher in the same vertical column.

Our task is to return only the visible nodes, starting from the leftmost column and moving towards the right.

Consider this tree:

```text
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
```

If we look at the tree from above, the visible nodes are:

```text
         4   2   1   3   7
```

Nodes `5` and `6` are hidden because node `1` is positioned above them in the same column.

The important thing here is that we don't need every node in the tree. We only need the first visible node at each horizontal distance.

## 2. The Key Observation: Why BFS?

Remember our Vertical Traversal problem? We tracked both row and column because we needed to collect every node and arrange them by position.

Top View is different.

We only need to know which node appears first in each column when looking from above.

This is where **Breadth-First Search (BFS)** becomes useful.

BFS visits nodes level by level:

```text
First:  Row 0
Then:   Row 1
Then:   Row 2
Then:   Row 3
```

Therefore, the first node encountered at a particular horizontal distance will always be at the minimum depth for that column.

Once we find that node, we don't need to replace it with any node encountered later.

$$
\color{#1f6feb}{\text{Top View = First BFS Node at Every Horizontal Distance}}
$$

This means we don't need to track the row coordinate explicitly. BFS already takes care of the top-to-bottom ordering.

## 3. Understanding Horizontal Distance

We assign a horizontal distance (column) to every node.

The root starts at column `0`.

- Moving left decreases the column by 1.
- Moving right increases the column by 1.

```python
# Root
queue = deque([(root, 0)])

# Left child
queue.append((node.left, col - 1))

# Right child
queue.append((node.right, col + 1))
```

For our example:

| Node | Horizontal Distance |
|---|---:|
| 1 | 0 |
| 2 | -1 |
| 3 | +1 |
| 4 | -2 |
| 5 | 0 |
| 6 | 0 |
| 7 | +2 |

Notice that nodes `1`, `5`, and `6` all belong to column `0`.

However, BFS encounters node `1` first. So node `1` becomes the visible node for that column.

## 4. Storing the Visible Nodes

We use a normal Python dictionary to store the first node encountered at each column.

```python
top_view = {}
```

As BFS processes each node, we check whether its column already exists.

```python
if col not in top_view:
    top_view[col] = node.val
```

Let's understand what happens.

When node `1` is encountered:

```python
top_view[0] = 1
```

Later, when node `5` is encountered at column `0`, the condition fails because column `0` already exists.

The same happens with node `6`.

This ensures that the first node is never overwritten.

After processing the complete tree, our dictionary becomes:

```python
{
     0: 1,
    -1: 2,
     1: 3,
    -2: 4,
     2: 7
}
```

The dictionary stores the correct visible nodes, but its keys are not necessarily in left-to-right order.

We solve that by sorting the columns.

## 5. Building the Final Answer

We sort the dictionary keys and collect their corresponding node values.

```python
result = [top_view[col] for col in sorted(top_view)]
```

For our example, the sorted columns are:

```python
[-2, -1, 0, 1, 2]
```

Their corresponding values are:

```python
[4, 2, 1, 3, 7]
```

**Final Output:**

```python
[4, 2, 1, 3, 7]
```

## 6. Complete Algorithm

Now the entire solution can be understood as a simple sequence:

1. Start BFS from the root at horizontal distance `0`.
2. Remove a node from the queue.
3. If its column has not been visited, store its value.
4. Add its left and right children with updated columns.
5. After BFS, sort the column keys.
6. Return the stored values from left to right.

```python
from collections import deque

def top_view(root):

    if root is None:
        return []

    top_view = {}
    queue = deque([(root, 0)])

    while queue:

        node, col = queue.popleft()

        if col not in top_view:
            top_view[col] = node.val

        if node.left:
            queue.append((node.left, col - 1))

        if node.right:
            queue.append((node.right, col + 1))

    return [top_view[col] for col in sorted(top_view)]
```

## 7. Complexity Analysis

Let \(N\) be the total number of nodes in the tree.

| Operation | Complexity |
|---|---|
| BFS traversal | \(O(N)\) |
| Sorting horizontal distances | \(O(N\log N)\) |
| Overall time | \(O(N\log N)\) |
| Auxiliary space | \(O(N)\) |
| Output space | \(O(N)\) |

Every node is visited exactly once. The additional sorting step arranges the horizontal distances from left to right.

## 8. Final Takeaway

The interesting part of Top View is that we don't need to calculate or store the row of every node.

In Vertical Traversal, we needed all nodes arranged by their coordinates. Here, we only need the first node encountered in each column.

BFS naturally guarantees that the first encountered node is the topmost one.

$$
\color{#1f6feb}{\text{BFS + Horizontal Distance + First Encounter}}
$$

This is the core pattern to remember for Top View of a Binary Tree.