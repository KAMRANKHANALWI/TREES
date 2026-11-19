# Nodes at Distance K

## 1. Understanding the Problem

Given a binary tree, a target node, and an integer $K$, find all nodes that are exactly $K$ edges away from the target node.

Distance is measured by the number of edges between two nodes.

Consider:

```text
                1
              /   \
             2     3
            / \     \
           4   5     6
              / \
             7   8
```

If our target is node `5` and $K=2$, we need to find all nodes that are two edges away from it.

```text
Distance 0:       5

Distance 1:     7, 8, 2

Distance 2:     4, 1
```

Therefore:

```python
Nodes at Distance 2 = [4, 1]
```

The interesting part is that we need to move both downwards and upwards in the tree.

## 2. The Key Observation: Parent Mapping + BFS

In normal Binary Tree BFS, we start from the root and move towards its left and right children.

However, this problem starts from an arbitrary target node. From that node, we may need to visit its parent as well.

Our usual `TreeNode` structure contains only:

```python
self.left
self.right
```

There is no direct reference to the parent.

So, how can we move upwards?

The solution is to first create a **Parent Mapping** using a dictionary.

```python
parent[child] = parent_node
```

For example:

```python
parent[5] = 2
parent[2] = 1
parent[7] = 5
```

Now, from any node, we can access its parent using the dictionary.

This allows us to explore three directions:

1. Left child
2. Right child
3. Parent

Once the parent mapping is ready, we perform BFS starting from the target node.

$$
\color{#1f6feb}{\text{Parent Mapping + BFS}}
$$

## 3. Step 1: Building the Parent Mapping

We use a separate BFS traversal to record the parent of every node.

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

Whenever we encounter a child, we store its parent.

For example, while processing node `2`:

```python
parent[node.left] = node
parent[node.right] = node
```

This creates:

```python
parent[4] = 2
parent[5] = 2
```

After processing the entire tree, every non-root node has its parent recorded.

The root is not included because it doesn't have a parent.

## 4. Step 2: BFS from the Target Node

Now that we can move upwards, we start a new BFS from the target.

```python
queue = deque([target])
visited = {target}
distance = 0
```

We initialize three things:

- `queue` stores nodes waiting to be explored.
- `visited` prevents revisiting nodes.
- `distance` tracks the current BFS level.

Initially:

```text
Queue:    [5]
Visited:  {5}
Distance: 0
```

### Why Do We Need a Visited Set?

In normal Tree BFS, we move only from parent to children. Since a tree has no cycles, revisiting a node is not possible.

But here, we can move in both directions.

For example:

$$
5 \rightarrow 2 \rightarrow 5
$$

When we move from node `5` to its parent `2`, node `2` can reach node `5` again through its right child.

Without a visited set, we would keep moving back and forth between them.

Therefore, before adding any neighbouring node to the queue, we check whether it has already been visited.

```python
if neighbour not in visited:
    visited.add(neighbour)
    queue.append(neighbour)
```

This ensures that every node is added to the queue at most once.

## 5. Step 3: Exploring All Three Directions

For every node removed from the queue, we explore its three possible neighbours.

**Direction 1: Left Child**

```python
if node.left and node.left not in visited:
    visited.add(node.left)
    queue.append(node.left)
```

**Direction 2: Right Child**

```python
if node.right and node.right not in visited:
    visited.add(node.right)
    queue.append(node.right)
```

These two operations are similar to normal Tree BFS. The only additional check is `visited`.

**Direction 3: Parent**

```python
if node in parent and parent[node] not in visited:
    visited.add(parent[node])
    queue.append(parent[node])
```

This is the additional part that makes the solution different from normal Tree BFS.

First, `node in parent` checks whether the current node has a parent. This is necessary because the root has no parent.

Then, `parent[node]` retrieves its parent from our dictionary.

Finally, we check whether that parent has already been visited before adding it to the queue.

$$
\color{#1f6feb}{\text{Neighbours = Left + Right + Parent}}
$$

## 6. Step 4: Controlling the BFS Distance

We don't want to traverse the entire tree. We only need to explore up to distance $K$.

For this, we use the familiar level-order traversal structure:

```python
while queue and distance < k:
    level_size = len(queue)

    for _ in range(level_size):
        node = queue.popleft()

        # Explore left, right and parent

    distance += 1
```

The important line is:

```python
level_size = len(queue)
```

It captures the number of nodes at the current distance.

Any new nodes added while processing this level belong to the next distance.

After processing the entire level, we increment `distance`.

Once `distance` reaches $K$, we stop exploring.

The queue now contains exactly the nodes at distance $K$.

## 7. Understanding the Complete BFS Dry Run

Let's find nodes at distance $2$ from target node `5`.

```text
                1
              /   \
             2     3
            / \     \
           4   5     6
              / \
             7   8
```

**Initial State**

```python
queue = [5]
visited = {5}
```

**Distance 0: Process Node 5**

Its three possible neighbours are:

- Left child → 7
- Right child → 8
- Parent → 2

All three are unvisited, so we add them.

```text
Queue: [7, 8, 2]
```

These nodes are at distance $1$.

**Distance 1: Process Nodes 7, 8 and 2**

- Node `7` → parent `5` (already visited).
- Node `8` → parent `5` (already visited).
- Node `2` → left child `4`, right child `5` (already visited), parent `1`.

Only nodes `4` and `1` are added.

```text
Queue: [4, 1]
```

These nodes are at distance $2$.

Since we have reached $K=2$, we stop.

The final queue contains:

```python
[4, 1]
```

**Final Answer:**

$$
\boxed{[4,1]}
$$

## 8. Complete Solution

```python
def nodes_at_distance_k(root, target, k):

    if root is None or target is None:
        return []

    # Step 1: Build parent mapping
    parent = build_parent_map(root)

    # Step 2: Start BFS from target
    queue = deque([target])
    visited = {target}
    distance = 0

    # Step 3: Explore exactly K levels
    while queue and distance < k:

        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # Explore left child
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)

            # Explore right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)

            # Explore parent
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                queue.append(parent[node])

        distance += 1

    return [node.val for node in queue]
```

Since `target` and the dictionary keys are TreeNode references, the mapping and visited set track actual node objects, not just their values.

## 9. Complexity Analysis

Let $N$ be the total number of nodes in the binary tree.

| Complexity | Value | Reason |
|---|---|---|
| Time | $O(N)$ | Parent mapping and BFS each visit nodes at most once |
| Auxiliary Space | $O(N)$ | Parent dictionary, visited set and BFS queue |

The parent mapping takes $O(N)$ time and space. The second BFS also takes at most $O(N)$ time and space.

## 10. Final Takeaway

The key to this problem is understanding why normal Tree BFS needs a small modification.

- **Parent Mapping:** Allows us to move upwards from a node.
- **BFS:** Explores nodes level by level according to their distance from the target.
- **Visited Set:** Prevents repeatedly moving between a parent and its child.
- **Level Size:** Ensures that we process exactly one distance level at a time.

$$
\boxed{\color{#1f6feb}{\text{Parent Mapping + BFS + Visited}}}
$$

Instead of starting from the root and moving only downwards, we convert the tree into a structure where every node can reach its parent and children. BFS then finds all nodes at the required distance.