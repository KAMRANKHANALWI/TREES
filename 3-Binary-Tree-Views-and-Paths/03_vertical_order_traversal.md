# Vertical Order Traversal of Binary Tree

## 1. Understanding the Problem

Imagine looking at a binary tree from the front and drawing an imaginary vertical line through every column of nodes.

Our task is to collect all nodes that fall along the same vertical line and return them column by column, starting from the leftmost column.

But there is one important detail: simply grouping nodes by their columns is not enough. We also need to know how high or low each node is. And if two nodes occupy exactly the same position, the smaller value must come first.

To solve this, we assign every node two coordinates:

- `row` tells us how far down the node is.
- `col` tells us how far left or right the node is.

We start the root at `(0, 0)`.

Whenever we move to a child:

- Moving left increases the row by 1 and decreases the column by 1.
- Moving right increases both the row and column by 1.

$$
\color{#1f6feb}{\text{Left Child} = (row+1,\ col-1)}
$$

$$
\color{#1f6feb}{\text{Right Child} = (row+1,\ col+1)}
$$

## 2. Why Do We Need BFS and Coordinates?

Consider this tree:

```text
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
```

We can calculate the coordinates by following the path from the root.

For example, node `5` is reached by moving left and then right:

- Start at node 1: `(0, 0)`
- Move left to node 2: `(1, -1)`
- Move right to node 5: `(2, 0)`

Similarly, node `6` is reached by moving right and then left:

- Start at node 1: `(0, 0)`
- Move right to node 3: `(1, 1)`
- Move left to node 6: `(2, 0)`

Notice something interesting: **nodes 5 and 6 have exactly the same coordinates `(2, 0)`.**

This is why we need to store multiple values at the same coordinate and sort them.

We use BFS because it naturally visits the tree level by level. Along with every node, we carry its row and column.

```python
queue = deque([(root, 0, 0)])
```

Each queue entry contains:

```python
(node, row, col)
```

As we process a node, we calculate the coordinates of its children and add them to the queue.

## 3. The Nested Dictionary: How Do We Store Everything?

Now that we know the coordinates, we need a data structure to organise the nodes.

Think of it like a filing cabinet:

- Every drawer represents a column.
- Every folder inside that drawer represents a row.
- Every folder contains the values of nodes at that exact coordinate.

We represent this using:

```python
nodes[col][row] = [values]
```

For example:

```python
nodes = {
    0: {
        0: [1],
        2: [5, 6]
    }
}
```

This tells us that column `0` contains:

- Node `1` at row `0`.
- Nodes `5` and `6` at row `2`.

But how do we avoid manually creating every dictionary and list?

This is where Python's `defaultdict` becomes useful.

```python
from collections import defaultdict

nodes = defaultdict(lambda: defaultdict(list))
```

Let's understand what happens when we write:

```python
nodes[0][2].append(5)
nodes[0][2].append(6)
```

If column `0` does not exist, Python automatically creates an inner dictionary. If row `2` does not exist, it automatically creates an empty list.

Both values are then stored in that same list.

Our complete storage operation becomes just one line:

```python
nodes[col][row].append(node.val)
```

## 4. Building the Nested Dictionary Using BFS

Now we can put the coordinate system and our storage structure together.

We start with the root at `(0, 0)` and process every node using a queue.

```python
nodes = defaultdict(lambda: defaultdict(list))

queue = deque([(root, 0, 0)])

while queue:

    node, row, col = queue.popleft()

    # Store the current node
    nodes[col][row].append(node.val)

    # Move left
    if node.left:
        queue.append((node.left, row + 1, col - 1))

    # Move right
    if node.right:
        queue.append((node.right, row + 1, col + 1))
```

After processing our example tree, the dictionary looks like this:

```python
{
    -2: {2: [4]},
    -1: {1: [2]},
     0: {0: [1], 2: [5, 6]},
     1: {1: [3]},
     2: {2: [7]}
}
```

At this point, every node is stored in the correct column and row. However, we still need to arrange the dictionary contents in the required order.

## 5. Converting the Dictionary into the Final Answer

Remember the three ordering rules from the problem:

1. Columns must go from left to right.
2. Within each column, rows must go from top to bottom.
3. If multiple nodes share the same coordinates, their values must be in ascending order.

Python's `sorted()` helps us achieve all three.

First, we sort the outer dictionary keys:

```python
for col in sorted(nodes):
```

This gives us the columns in left-to-right order: `-2, -1, 0, 1, 2`.

Next, inside each column, we sort the row keys:

```python
for row in sorted(nodes[col]):
```

This ensures that nodes are collected from top to bottom.

Finally, we sort the values stored at that coordinate:

```python
values = sorted(nodes[col][row])
```

This handles cases like nodes `5` and `6` that occupy the same position.

We then use `extend()` to add all those values to the current column.

```python
result = []

for col in sorted(nodes):

    column = []

    for row in sorted(nodes[col]):

        values = sorted(nodes[col][row])

        column.extend(values)

    result.append(column)

return result
```

The final result becomes:

```python
[[4], [2], [1, 5, 6], [3], [7]]
```

## 6. Complete Algorithm

The entire problem can now be understood as two major operations:

**First:** Use BFS to discover every node's coordinates and store its value in the nested dictionary.

**Second:** Sort the columns, rows and values to construct the final answer.

$$
\color{#1f6feb}{\text{BFS} \rightarrow \text{Coordinate Mapping} \rightarrow \text{Grouping} \rightarrow \text{Sorting}}
$$

## 7. Complexity Analysis

Let \(N\) be the total number of nodes in the tree.

| Operation | Complexity |
|---|---|
| BFS traversal | \(O(N)\) |
| Sorting columns, rows and coordinate values | \(O(N\log N)\) upper bound |
| Overall time | \(O(N\log N)\) |
| Auxiliary space | \(O(N)\) |
| Output space | \(O(N)\) |

Every node is visited once during BFS. The additional work comes from sorting the stored coordinates and values.

## 8. Final Takeaway

The most important thing to understand in this problem is that **we are not just traversing a tree; we are assigning a position to every node and grouping nodes by that position.**

BFS helps us discover those positions, the nested `defaultdict` helps us organise them, and sorting helps us produce the required vertical order.

Once this coordinate-based pattern becomes clear, it becomes much easier to approach other tree problems involving columns, rows, views and positional relationships.