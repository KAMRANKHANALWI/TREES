# Burning Tree

## 1. Understanding the Problem

We are given a binary tree and a target node where the fire starts.

The fire spreads to its adjacent nodes every second. A node can catch fire from:

1. Its left child.
2. Its right child.
3. Its parent.

Our task is to find the **minimum time required to burn the entire binary tree**.

Consider the following tree:

```text
                  1
                /   \
               2     3
              / \     \
             4   5     6
                / \
               7   8
```

Suppose the fire starts at node `5`.

The fire spreads as follows:

| Time | Newly burning nodes |
|---|---|
| 0 | `[5]` |
| 1 | `[7, 8, 2]` |
| 2 | `[4, 1]` |
| 3 | `[3]` |
| 4 | `[6]` |

At time `4`, every node has caught fire.

Therefore:

$$
\boxed{\text{Minimum Burning Time} = 4}
$$

The important thing to understand is that fire spreads in all three directions: left, right, and parent.

## 2. Key Observation: Parent Mapping + BFS

In a normal binary tree, we can move only downwards using the left and right pointers.

However, in this problem, fire can also spread upwards to the parent.

For example, starting from node `5`:

- Left child: `7`
- Right child: `8`
- Parent: `2`

The problem is that a binary tree node does not directly store a pointer to its parent.

We solve this by combining two techniques:

1. **Parent Mapping:** Store the parent of every node so that we can move upwards.
2. **BFS:** Start from the target and explore all reachable nodes level by level.

The key observation is:

$$
\color{#1f6feb}{\text{Every BFS level represents one second of fire spreading.}}
$$

We continue BFS until every node has been visited.

Unlike Nodes at Distance K, we do not stop at a particular distance. We need to reach the entire tree.

## 3. Step 1: Building the Parent Mapping

First, we need to know the parent of every node.

We use BFS to traverse the tree and store the parent-child relationship in a dictionary.

For our example, the mapping will look like this:

```text
parent[2] = 1
parent[3] = 1
parent[4] = 2
parent[5] = 2
parent[6] = 3
parent[7] = 5
parent[8] = 5
```

Here, the child node is the dictionary key, and its parent node is the corresponding value.

For example:

```python
parent[node.left] = node
```

This means that the left child of the current node has the current node as its parent.

### Helper Function

```python
def build_parent_map(root):
    parent = {}
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            parent[node.left] = node
            queue.append(node.left)

        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    return parent
```

Let's understand the important parts:

- `parent = {}` creates an empty dictionary.
- `queue = deque([root])` starts BFS from the root.
- `parent[node.left] = node` stores the parent of the left child.
- `parent[node.right] = node` stores the parent of the right child.
- Both children are added to the queue so that we can process their children as well.

The root does not appear as a key because it has no parent.

We use node objects as dictionary keys instead of node values. This is important because different nodes may contain the same value.

After this function finishes, we can access the parent of any non-root node in constant average time.

## 4. Step 2: Starting BFS from the Target

Once the parent mapping is ready, we start BFS from the target node.

```python
queue = deque([target])
visited = {target}

time = 0
```

Let's understand these variables:

- `queue`: Stores nodes that are burning or waiting to spread fire.
- `visited`: Stores nodes that have already caught fire.
- `time`: Tracks the total number of seconds required for spreading.

Initially, only the target node is burning.

```text
queue    = [5]
visited  = {5}
time     = 0
```

We use a visited set because fire can move both upwards and downwards.

Without it, we could repeatedly move between a child and its parent.

For example:

```text
5 → 2 → 5 → 2 → ...
```

The visited set prevents this cycle.

We mark a node as visited when adding it to the queue, ensuring that it is never added more than once.

## 5. Step 3: Exploring All Three Directions

For every burning node, we check three possible directions.

### Direction 1: Left Child

```python
if node.left and node.left not in visited:
    visited.add(node.left)
    queue.append(node.left)
    burned_something = True
```

If the left child exists and has not caught fire, we add it to the queue.

### Direction 2: Right Child

```python
if node.right and node.right not in visited:
    visited.add(node.right)
    queue.append(node.right)
    burned_something = True
```

Similarly, we add the right child if it exists and is unvisited.

### Direction 3: Parent

```python
if node in parent and parent[node] not in visited:
    visited.add(parent[node])
    queue.append(parent[node])
    burned_something = True
```

This is the additional direction that makes this problem different from normal tree BFS.

Let's understand it:

- `node in parent` checks whether the current node has a parent.
- `parent[node]` retrieves its parent.
- `parent[node] not in visited` ensures that the parent has not already caught fire.
- We add the parent to both the visited set and queue.

Therefore, every node can spread fire in three directions:

$$
\color{#1f6feb}{\text{Left} \;+\; \text{Right} \;+\; \text{Parent}}
$$

## 6. Step 4: Controlling BFS Levels and Time

This is the most important part of the solution.

We need to process all nodes at the current level before moving to the next level.

```python
while queue:
    level_size = len(queue)
    burned_something = False

    for _ in range(level_size):
        node = queue.popleft()

        # Explore left, right and parent

    if burned_something:
        time += 1
```

### Why Do We Use `level_size`?

At the beginning of every iteration, the queue contains all nodes that are currently burning at the same time.

We store its size:

```python
level_size = len(queue)
```

Then we process exactly that many nodes:

```python
for _ in range(level_size):
    node = queue.popleft()
```

Any newly discovered nodes are added to the back of the queue.

However, they are not processed in the current iteration. They will be processed in the next iteration, representing the next second.

This is how BFS maintains the correct timing of fire spreading.

### Why Do We Need `burned_something`?

Consider the final stage of the tree.

Eventually, some nodes will be burning, but none of them will have any unburnt neighbours.

We still need to process those nodes, but no additional second is required for spreading.

Therefore, we use:

```python
burned_something = False
```

Whenever a new node catches fire, we update it:

```python
burned_something = True
```

After processing the complete level:

```python
if burned_something:
    time += 1
```

This ensures that we increment time only when fire actually spreads to at least one new node.

**Important:** Without this condition, we would count one extra second after processing the final burning level.

## 7. Complete BFS Dry Run

Let's perform a complete dry run using the same example.

Target node = `5`

```text
                  1
                /   \
               2     3
              / \     \
             4   5     6
                / \
               7   8
```

### Initial State

```text
queue    = [5]
visited  = {5}
time     = 0
```

Only node `5` is burning.

### Time 0 → Time 1

Process node `5`.

Its neighbours are:

- Left child: `7`
- Right child: `8`
- Parent: `2`

All three nodes catch fire.

```text
queue = [7, 8, 2]
visited = {5, 7, 8, 2}
```

Since new nodes caught fire:

```python
time = 1
```

### Time 1 → Time 2

Now process the current level: `[7, 8, 2]`.

**Process node 7:**

- Parent is `5`, already visited.
- No children.

No new node catches fire.

**Process node 8:**

- Parent is `5`, already visited.
- No children.

No new node catches fire.

**Process node 2:**

- Left child is `4`.
- Right child is `5`, already visited.
- Parent is `1`.

Nodes `4` and `1` catch fire.

```text
queue = [4, 1]
visited = {5, 7, 8, 2, 4, 1}
```

Since new nodes caught fire:

```python
time = 2
```

### Time 2 → Time 3

Process the current level: `[4, 1]`.

**Process node 4:**

- Parent is `2`, already visited.
- No children.

**Process node 1:**

- Left child is `2`, already visited.
- Right child is `3`.

Node `3` catches fire.

```text
queue = [3]
visited = {5, 7, 8, 2, 4, 1, 3}
```

Since a new node caught fire:

```python
time = 3
```

### Time 3 → Time 4

Process node `3`.

- Left child does not exist.
- Right child is `6`.
- Parent is `1`, already visited.

Node `6` catches fire.

```text
queue = [6]
visited = {5, 7, 8, 2, 4, 1, 3, 6}
```

Since a new node caught fire:

```python
time = 4
```

### Final Level

Now process node `6`.

- No children.
- Parent is `3`, already visited.

No new node catches fire.

Therefore:

```python
burned_something = False
```

Time is not incremented.

The queue becomes empty, and BFS finishes.

**Final Answer:**

$$
\boxed{\text{Burning Time} = 4}
$$

## 8. Complete Python Solution

```python
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_parent_map(root):
    parent = {}
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            parent[node.left] = node
            queue.append(node.left)

        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    return parent


def burning_tree(root, target):
    if root is None or target is None:
        return 0

    parent = build_parent_map(root)

    queue = deque([target])
    visited = {target}

    time = 0

    while queue:
        level_size = len(queue)
        burned_something = False

        for _ in range(level_size):
            node = queue.popleft()

            # Left child
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)
                burned_something = True

            # Right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)
                burned_something = True

            # Parent
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                queue.append(parent[node])
                burned_something = True

        if burned_something:
            time += 1

    return time


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    target = root.left.right

    print("Burning Time:", burning_tree(root, target))
```

### Output

```text
Burning Time: 4
```

## 9. Complexity Analysis

Let $N$ be the total number of nodes in the binary tree.

| Operation | Time Complexity |
|---|---|
| Building parent mapping | $O(N)$ |
| BFS traversal | $O(N)$ |
| Total | $O(N)$ |

Every node is processed once during parent mapping and at most once during the burning BFS.

Therefore:

**Time Complexity:**

$$
O(N) + O(N) = \boxed{O(N)}
$$

**Space Complexity:**

We use:

- Parent mapping: $O(N)$
- BFS queue: $O(N)$
- Visited set: $O(N)$

Therefore:

$$
\boxed{O(N)}
$$

## 10. Final Takeaway

Burning Tree is an extension of the Nodes at Distance K problem.

Both problems use the same fundamental technique:

1. Build a parent mapping to enable upward movement.
2. Start BFS from the target node.
3. Explore left child, right child, and parent.
4. Use a visited set to prevent repeated visits.
5. Process BFS level by level.

The only major difference is how we use the BFS result.

| Nodes at Distance K | Burning Tree |
|---|---|
| Stop at distance `K` | Continue until BFS finishes |
| Return nodes at distance `K` | Return total burning time |
| Track distance | Track time |

The core pattern to remember is:

$$
\color{#1f6feb}{\text{Parent Mapping + BFS + Visited + Level Order}}
$$

**Key learning:** When a problem asks us to spread something through a binary tree in all directions, think about converting the tree into a graph using parent mapping, then applying BFS.