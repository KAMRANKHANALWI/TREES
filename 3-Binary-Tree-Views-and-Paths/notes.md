# Binary Tree Views and Paths Notes

This section is mainly about **traversing trees with extra information** — levels, horizontal distance, coordinates, parents, paths, and pointer connections.

| # | Problem | Pattern |
|---|---|---|
| 01 | Zigzag Traversal | BFS + alternating direction |
| 02 | Boundary Traversal | Boundary + leaf traversal |
| 03 | Vertical Order Traversal | BFS + coordinates + sorting |
| 04 | Top View | BFS + horizontal distance |
| 05 | Bottom View | BFS + horizontal distance + overwrite |
| 06 | Left / Right View | BFS + first/last node per level |
| 07 | Root-to-Leaf Path | DFS + backtracking |
| 08 | Lowest Common Ancestor | Recursive DFS |
| 09 | Maximum Width | BFS + positional indexing |
| 10 | Nodes at Distance K | Parent mapping + BFS |
| 11 | Burning Tree | Parent mapping + BFS levels |
| 12 | Count Nodes in Complete Binary Tree | Height + perfect subtree detection |
| 13 | Flatten Binary Tree | In-place pointer manipulation |

---

## 01. Zigzag Traversal

Normal Level Order Traversal uses BFS. Zigzag changes the direction of output at every level, but the queue remains normal.

Use the index to place values in the correct position.

```python
def zigzag(root):
    if not root: return []

    q = deque([root])
    result = []
    left_to_right = True

    while q:
        size = len(q)
        level = [0] * size

        for i in range(size):
            node = q.popleft()

            idx = i if left_to_right else size - 1 - i
            level[idx] = node.val

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        result.append(level)
        left_to_right = not left_to_right

    return result
```

**Key:** Don't reverse the queue. Only reverse the position where values are placed.

O(N) time, O(N) space.

---

## 02. Boundary Traversal

Anti-clockwise boundary = root + left boundary + leaves + reversed right boundary.

Avoid duplicate nodes, especially leaves.

```python
def is_leaf(node):
    return not node.left and not node.right

def boundary(root):
    if not root: return []

    ans = [root.val]

    # Left boundary (exclude leaves)
    node = root.left
    while node:
        if not is_leaf(node): ans.append(node.val)
        node = node.left if node.left else node.right

    # All leaves: left to right
    def leaves(node):
        if not node: return
        if is_leaf(node):
            ans.append(node.val)
            return
        leaves(node.left)
        leaves(node.right)

    leaves(root)

    # Right boundary (exclude leaves), reversed
    temp = []
    node = root.right
    while node:
        if not is_leaf(node): temp.append(node.val)
        node = node.right if node.right else node.left

    ans.extend(reversed(temp))
    return ans
```

**Order:** root → left boundary → leaves → right boundary bottom-up.

O(N) time, O(H) auxiliary space (excluding output).

---

## 03. Vertical Order Traversal

Assign each node coordinates `(row, col)`.

- Root: `(0, 0)`
- Left child: `(row + 1, col - 1)`
- Right child: `(row + 1, col + 1)`

Store values using:

```python
nodes[col][row] = [values]
```

Then sort:

1. Columns from left to right.
2. Rows from top to bottom.
3. Values at the same row and column.

```python
nodes = defaultdict(lambda: defaultdict(list))
q = deque([(root, 0, 0)])  # node, row, col

while q:
    node, row, col = q.popleft()
    nodes[col][row].append(node.val)

    if node.left:
        q.append((node.left, row + 1, col - 1)
    if node.right:
        q.append((node.right, row + 1, col + 1)

ans = []

for col in sorted(nodes):
    column = []
    for row in sorted(nodes[col]):
        column.extend(sorted(nodes[col][row]))
    ans.append(column)
```

**Key:** Coordinates tell us where a node belongs. Sorting resolves the required order.

O(N log N) time, O(N) space.

---

## 04. Top View

Top view = first node encountered at every horizontal distance (column).

Use BFS because it visits nodes level by level. The first node at a column is the topmost node.

```python
def top_view(root):
    if not root: return []

    q = deque([(root, 0)])
    view = {}

    while q:
        node, col = q.popleft()

        if col not in view:
            view[col] = node.val

        if node.left: q.append((node.left, col - 1))
        if node.right: q.append((node.right, col + 1)

    return [view[c] for c in sorted(view)]
```

**Key:** Store only if the column hasn't been seen before.

O(N log N) time including column sorting, O(N) space.

---

## 05. Bottom View

Bottom view = last node encountered at every horizontal distance.

Same BFS and column logic as Top View, but overwrite every time.

```python
def bottom_view(root):
    if not root: return []

    q = deque([(root, 0)])
    view = {}

    while q:
        node, col = q.popleft()
        view[col] = node.val       # overwrite

        if node.left: q.append((node.left, col - 1))
        if node.right: q.append((node.right, col + 1)

    return [view[c] for c in sorted(view)]
```

**Top vs Bottom:**

| Top View | Bottom View |
|---|---|
| Store first value | Store last value |
| `if col not in view` | `view[col] = node.val` |
| BFS | BFS |

When nodes have the same depth and column, later BFS nodes overwrite earlier ones.

O(N log N) time including sorting, O(N) space.

---

## 06. Left and Right View

One node per level.

- Left view: first node at every level.
- Right view: last node at every level.

```python
def left_view(root):
    if not root: return []

    q = deque([root])
    ans = []

    while q:
        size = len(q)

        for i in range(size):
            node = q.popleft()

            if i == 0:
                ans.append(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    return ans
```

For right view, change:

```python
if i == size - 1:
    ans.append(node.val)
```

**Key:** `size` represents the current level. Don't use the total queue size after processing nodes.

O(N) time, O(N) space.

---

## 07. Root-to-Leaf Path / Root-to-Target Path

DFS + backtracking. Maintain a path from root to current node.

```python
def find_path(root, target, path):
    if not root: return False

    path.append(root.val)

    if root.val == target:
        return True

    if find_path(root.left, target, path): return True
    if find_path(root.right, target, path): return True

    path.pop()             # backtrack
    return False
```

**Why `pop()`?** If a node doesn't lead to the target, remove it so the path represents the correct branch.

The path is built on entry and cleaned up when a branch fails.

O(N) time, O(H) recursion space, plus path.

---

## 08. Lowest Common Ancestor (LCA)

Find the lowest node that is an ancestor of both `p` and `q`.

```python
def lca(root, p, q):
    if not root: return None

    if root is p or root is q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    if left: return left
    return right
```

**The three cases:**

| Left result | Right result | Return |
|---|---|---|
| Found | Found | Current node (LCA) |
| Found | None | Left result |
| None | Found | Right result |
| None | None | None |

If `p` and `q` are found in different subtrees, current node is their LCA. If one is an ancestor of the other, that node itself is returned.

O(N) time, O(H) space.

---

## 09. Maximum Width of Binary Tree

Width includes gaps between the leftmost and rightmost nodes at a level.

Treat positions like a complete binary tree:

```text
root index = 0
left  = 2*i + 1
right = 2*i + 2
```

Width of a level:

```python
width = last_index - first_index + 1
```

```python
def width_of_tree(root):
    if not root: return 0

    q = deque([(root, 0)])
    ans = 0

    while q:
        size = len(q)
        first = q[0][1]
        last = q[-1][1]

        ans = max(ans, last - first + 1)

        for _ in range(size):
            node, idx = q.popleft()
            idx -= first          # normalize

            if node.left:
                q.append((node.left, 2 * idx + 1)
            if node.right:
                q.append((node.right, 2 * idx + 2)

    return ans
```

**Normalization:** subtracting the first index from every index at the level keeps relative distances the same while preventing huge indices.

O(N) time, O(N) space.

---

## 10. Nodes at Distance K

A normal tree traversal only moves downward. To move in all directions from the target, create a parent mapping.

### Step 1: Build parents

```python
parent = {}

q = deque([root])

while q:
    node = q.popleft()

    if node.left:
        parent[node.left] = node
        q.append(node.left)

    if node.right:
        parent[node.right] = node
        q.append(node.right)
```

### Step 2: BFS from target

Possible directions:

- Left
- Right
- Parent

```python
q = deque([target])
visited = {target}
distance = 0

while q and distance < k:
    size = len(q)

    for _ in range(size):
        node = q.popleft()

        for neighbor in (node.left, node.right, parent.get(node)):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    distance += 1

return [node.val for node in q]
```

**Why visited?** Parent links introduce cycles: `child → parent → child`. Mark nodes visited when enqueuing.

**Why level-by-level?** Each BFS level represents one unit of distance.

O(N) time, O(N) space.

---

## 11. Burning Tree

Fire starts at a target node. Each second, it spreads to left, right, and parent.

Same pattern as Nodes at Distance K:

1. Build parent mapping.
2. BFS from target.
3. Explore left, right, parent.
4. Track levels/time.

```python
time = 0

while q:
    size = len(q)
    burned_something = False

    for _ in range(size):
        node = q.popleft()

        for neighbor in (node.left, node.right, parent.get(node)):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                burned_something = True

    if burned_something:
        time += 1
```

`burned_something` prevents adding an extra second when processing the final level, where no new node catches fire.

**Connection to Problem 10:** Nodes at distance K asks for a particular BFS level. Burning Tree asks how many levels are needed to reach the farthest node.

O(N) time, O(N) space.

---

## 12. Count Nodes in Complete Binary Tree

A complete tree has all levels filled except possibly the last, which is filled from left to right.

**Key optimization:** If leftmost height = rightmost height, the subtree is perfect.

Number of nodes in a perfect tree:

$$
2^H - 1
$$

```python
def left_height(node):
    h = 0
    while node:
        h += 1
        node = node.left
    return h

def right_height(node):
    h = 0
    while node:
        h += 1
        node = node.right
    return h

def count_nodes(root):
    if not root: return 0

    lh = left_height(root)
    rh = right_height(root)

    if lh == rh:
        return (1 << lh) - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

Equal heights ⇒ perfect subtree, count directly. Otherwise recurse.

**Important:** This shortcut is valid because the input is guaranteed to be complete.

O(log² N) time, O(log N) space.

---

## 13. Flatten Binary Tree to Linked List

Flatten in preorder, in-place. All left pointers become `None`, and right pointers form the preorder chain.

At each node:

1. Save original right subtree.
2. Move left subtree to right.
3. Clear left pointer.
4. Find rightmost node of moved subtree.
5. Attach original right subtree.
6. Move forward.

```python
def flatten(root):
    curr = root

    while curr:
        if curr.left:
            right_subtree = curr.right

            curr.right = curr.left
            curr.left = None

            temp = curr.right
            while temp.right:
                temp = temp.right

            temp.right = right_subtree

        curr = curr.right
```

**Why save `curr.right` first?** Because overwriting it with the left subtree would otherwise lose the original right subtree.

**Why attach to the rightmost node?** Preorder requires the entire left subtree to come before the original right subtree.

O(N²) worst-case time for this approach, O(1) space.

---

## Cheat Sheet

| Problem | Main idea | Complexity |
|---|---|---|
| Zigzag | BFS + alternating index | O(N) |
| Boundary | Root + boundaries + leaves | O(N) |
| Vertical | Coordinates + sorting | O(N log N) |
| Top View | First per column | O(N log N) |
| Bottom View | Last per column | O(N log N) |
| Left / Right View | First/last per level | O(N) |
| Root-to-Target Path | DFS + backtracking | O(N) |
| LCA | Recursive result from both sides | O(N) |
| Maximum Width | Complete-tree indices | O(N) |
| Distance K | Parent mapping + BFS | O(N) |
| Burning Tree | Parent mapping + BFS levels | O(N) |
| Count Complete Nodes | Heights + perfect-tree formula | O(log² N) |
| Flatten | In-place pointer rearrangement | O(N²) worst |

## Patterns to Remember

**BFS + Level Size**

Use whenever the problem asks about levels, views, zigzag, distance, or burning time.

```python
size = len(q)
for _ in range(size):
    ...
```

**BFS + Horizontal Distance**

Use for Top View, Bottom View, and Vertical Order.

```python
left:  col - 1
right: col + 1
```

**DFS + Backtracking**

Use when maintaining a path and undoing choices when returning from unsuccessful branches.

**Parent Mapping + BFS**

Use when movement must happen both downward and upward: Distance K and Burning Tree.

**Tree Property + Optimization**

Complete Binary Tree allows us to count perfect subtrees directly.

**Pointer Manipulation**

Flattening rearranges the existing nodes without a traversal output list.

## Complexity

Let N = number of nodes and H = tree height.

| Pattern | Time | Space |
|---|---|---|
| Standard BFS / DFS | O(N) | O(N) / O(H) |
| BFS + sorting columns | O(N log N) | O(N) |
| Parent map + BFS | O(N) | O(N) |
| Complete tree counting | O(log² N) | O(log N) |
| Flatten (current approach) | O(N²) worst | O(1) |

## Python Bits

- `deque`: efficient queue for BFS (`popleft()`).
- `defaultdict`: nested coordinate maps without manual initialization.
- `set`: `visited` prevents cycles when traversing parents.
- `nonlocal`: lets nested recursion update an outer variable.
- `node is target`: compares object identity, useful when targeting a specific node.
- `q[0]` / `q[-1]`: first and last items in a level when the queue contains that level.
- `2*i + 1`, `2*i + 2`: complete-tree positional indices.
- `1 << H`: computes $2^H$.
- `temp.right`: pointer rearrangement without creating new nodes.

**Overall:** Most of this section is BFS with a small extra piece of information. Identify what information each node needs (level, column, coordinate, parent, index, path), and the traversal usually becomes straightforward.