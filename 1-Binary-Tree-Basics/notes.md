# Binary Tree Basics — Theory & Traversals

## 1. Introduction to Binary Trees

### What is a Tree?

A Tree is a non-linear hierarchical data structure consisting of nodes connected through edges.

Unlike arrays and linked lists, trees represent hierarchical relationships.

### Basic Terminology

Consider the following tree:

```text
                 1              <- Root
               /   \
              2     3           <- Children of 1
             / \   / \
            4   5 6   7         <- Leaf Nodes
```

| Term | Meaning |
|---|---|
| Root | Topmost node of the tree |
| Parent | A node that has children |
| Child | A node directly connected below a parent |
| Leaf | A node with no children |
| Sibling | Nodes sharing the same parent |
| Edge | Connection between two nodes |
| Ancestor | Any predecessor on the path to a node |
| Descendant | Any node below a particular node |
| Subtree | A node together with its descendants |
| Depth | Number of edges from root to a node |
| Height | Number of edges on the longest downward path to a leaf |

### What is a Binary Tree?

A Binary Tree is a tree in which each node can have at most two children:

- Left Child
- Right Child

A node can have:
- No children
- Only a left child
- Only a right child
- Both children

### Python Representation

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

Each node contains:

- `val`: Stores the node's value.
- `left`: Reference to the left child.
- `right`: Reference to the right child.

### Constructing a Binary Tree

```python
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
```

Result:

```text
                 1
               /   \
              2     3
             / \   / \
            4   5 6   7
```

---

## 2. Types of Binary Trees

### 2.1 Full Binary Tree

Every node has either:
- Zero children, or
- Exactly two children.

```text
          1
        /   \
       2     3
      / \
     4   5
```

Node `2` has two children, while nodes `3`, `4`, and `5` are leaves.

### 2.2 Complete Binary Tree

Every level is completely filled except possibly the last level.

The last level must be filled from left to right without gaps.

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

This is a Complete Binary Tree.

### 2.3 Perfect Binary Tree

Every internal node has exactly two children, and all leaf nodes are at the same level.

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

For a perfect binary tree:

- Every level is completely filled.
- Number of nodes at level `L` = $2^L$, assuming root is level 0.
- Total nodes for height `h` measured in edges:

$$
\color{#1f6feb}{N = 2^{h+1}-1}
$$

### 2.4 Balanced Binary Tree

A binary tree is height-balanced if, at every node, the height difference between its left and right subtrees is at most 1.

$$
\color{#1f6feb}{|H(left)-H(right)| \leq 1}
$$

Example:

```text
          1
        /   \
       2     3
      /
     4
```

### 2.5 Degenerate / Skewed Binary Tree

A tree in which every parent has only one child.

Left-skewed:

```text
       1
      /
     2
    /
   3
  /
 4
```

Right-skewed:

```text
1
 \
  2
   \
    3
     \
      4
```

A degenerate tree behaves similarly to a linked list.

Its height can become $O(N)$.

---

## 3. Binary Tree Traversals

Traversal means visiting every node of a tree in a particular order.

There are two major categories:

### DFS — Depth First Search

Explore a branch deeply before moving to another branch.

Three fundamental DFS traversals:

1. Preorder
2. Inorder
3. Postorder

### BFS — Breadth First Search

Visit nodes level by level.

Main traversal:

1. Level Order Traversal

---

## 4. Preorder Traversal

### Pattern

$\color{#1f6feb}{\textbf{Root} \rightarrow \textbf{Left} \rightarrow \textbf{Right}}$

Process the current node immediately, before visiting its children.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Execution:

1. Visit `1`
2. Go left → visit `2`
3. Go left → visit `4`
4. Backtrack → visit `5`
5. Backtrack to root → visit `3`
6. Visit `6`
7. Visit `7`

Output:

```python
[1, 2, 4, 5, 3, 6, 7]
```

### Recursive Implementation

```python
def preorder(root, ans):
    if root is None:
        return

    ans.append(root.val)

    preorder(root.left, ans)
    preorder(root.right, ans)

    return ans
```

### Key Observation

$\color{#1f6feb}{\text{The current node is appended before either recursive call.}}$

```python
ans.append(root.val)

preorder(root.left, ans)
preorder(root.right, ans)
```

### Iterative Implementation

Use a stack.

```python
def preorder_iterative(root):
    if root is None:
        return []

    stack = [root]
    ans = []

    while stack:
        node = stack.pop()

        ans.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return ans
```

$\color{#1f6feb}{\textbf{Why push right before left?}}$

A stack follows LIFO (Last In, First Out).

Pushing right first ensures the left child is popped and processed first.

### Complexity

| Complexity | Value |
|---|---|
| Time | O(N) |
| Recursive auxiliary space | O(H) |
| Iterative auxiliary space | O(H) typical DFS stack bound |
| Output | O(N) |

---

## 5. Inorder Traversal

### Pattern

$\color{#1f6feb}{\textbf{Left} \rightarrow \textbf{Root} \rightarrow \textbf{Right}}$

Process the current node after completing its left subtree but before visiting its right subtree.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Execution:

1. Go left until node `4`.
2. Visit `4`.
3. Return to `2` and visit `2`.
4. Visit `5`.
5. Return to `1` and visit `1`.
6. Visit `6`.
7. Visit `3`.
8. Visit `7`.

Output:

```python
[4, 2, 5, 1, 6, 3, 7]
```

### Recursive Implementation

```python
def inorder(root, ans):
    if root is None:
        return

    inorder(root.left, ans)

    ans.append(root.val)

    inorder(root.right, ans)

    return ans
```

### Key Observation

$\color{#1f6feb}{\text{The current node is appended between the left and right recursive calls.}}$

### Iterative Implementation

Use a stack to simulate recursive traversal.

```python
def inorder_iterative(root):
    stack = []
    ans = []
    current = root

    while current or stack:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        ans.append(current.val)

        current = current.right

    return ans
```

### Understanding the Iterative Logic

1. Keep moving left while pushing nodes onto the stack.
2. When there is no more left child, pop a node.
3. Process the popped node.
4. Move to its right child.
5. Repeat until both `current` and `stack` are empty.

### Important Property of BST

$\color{#1f6feb}{\text{For a BST, inorder traversal gives values in sorted ascending order (standard strict key ordering).}}$

### Complexity

| Complexity | Value |
|---|---|
| Time | O(N) |
| Recursive auxiliary space | O(H) |
| Iterative auxiliary space | O(H) |
| Output | O(N) |

---

## 6. Postorder Traversal

### Pattern

$\color{#1f6feb}{\textbf{Left} \rightarrow \textbf{Right} \rightarrow \textbf{Root}}$

Process the current node only after both subtrees have been completed.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Execution:

1. Visit left subtree of `1`.
2. Visit `4`.
3. Visit `5`.
4. Visit `2`.
5. Visit `6`.
6. Visit `7`.
7. Visit `3`.
8. Finally visit `1`.

Output:

```python
[4, 5, 2, 6, 7, 3, 1]
```

### Recursive Implementation

```python
def postorder(root, ans):
    if root is None:
        return

    postorder(root.left, ans)

    postorder(root.right, ans)

    ans.append(root.val)

    return ans
```

### Key Observation

$\color{#1f6feb}{\text{The current node is appended after both recursive calls.}}$

### Iterative Implementation — Two Stacks

```python
def postorder_iterative(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()

        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    ans = []

    while stack2:
        ans.append(stack2.pop().val)

    return ans
```

### Why Two Stacks?

The first stack creates a reverse-like traversal order:

$\color{#1f6feb}{\textbf{Root} \rightarrow \textbf{Right} \rightarrow \textbf{Left}}$

The second stack reverses it:

$\color{#1f6feb}{\textbf{Left} \rightarrow \textbf{Right} \rightarrow \textbf{Root}}$

This produces postorder.

### Complexity

| Complexity | Value |
|---|---|
| Time | O(N) |
| Recursive auxiliary space | O(H) |
| Iterative auxiliary space | O(N) |
| Output | O(N) |

---

## 7. Level Order Traversal

### Pattern

$\color{#1f6feb}{\textbf{BFS — Breadth First Search}}$

Visit nodes level by level, from left to right.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Expected output:

```python
[
    [1],
    [2, 3],
    [4, 5, 6, 7]
]
```

### Key Observation

$\color{#1f6feb}{\text{Unlike DFS, BFS does not go deep into one branch immediately.}}$

It processes every node at the current level before moving to the next level.

### Why Queue?

A queue follows FIFO (First In, First Out).

The first discovered node is processed first.

Python implementation:

```python
from collections import deque
```

### Implementation

```python
from collections import deque


def level_order(root):
    if root is None:
        return []

    queue = deque([root])
    ans = []

    while queue:

        level_size = len(queue)
        level = []

        for _ in range(level_size):

            node = queue.popleft()

            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        ans.append(level)

    return ans
```

### Understanding `level_size`

$\color{#1f6feb}{\textbf{This is the most important part:}}$

```python
level_size = len(queue)

for _ in range(level_size):
```

Suppose:

```python
queue = [2, 3]
```

Then:

```python
level_size = 2
```

We process exactly two nodes.

While processing these nodes, their children are added to the queue, but they are not processed until the next outer loop iteration.

This is how we separate levels.

### Complexity

| Complexity | Value |
|---|---|
| Time | O(N) |
| Auxiliary space | O(N) |
| Output | O(N) |

---

## 8. All Three DFS Traversals in One Traversal

### Problem

Calculate preorder, inorder and postorder simultaneously using one iterative traversal.

### Key Observation

$\color{#1f6feb}{\text{Every node is processed at three different stages.}}$

We can use a stack containing:

```python
(node, state)
```

The state determines which traversal operation should happen next.

| State | Traversal | Action |
|---|---|---|
| 1 | Preorder | Append node |
| 2 | Inorder | Append node |
| 3 | Postorder | Append node |

### State 1 — Preorder

```python
preorder.append(node.val)

stack.append((node, 2))

if node.left:
    stack.append((node.left, 1))
```

Process the node first, then visit its left subtree.

### State 2 — Inorder

```python
inorder.append(node.val)

stack.append((node, 3))

if node.right:
    stack.append((node.right, 1))
```

Process the node between its left and right subtrees.

### State 3 — Postorder

```python
postorder.append(node.val)
```

Both subtrees have already been processed.

### Complete Implementation

```python
def all_traversals(root):
    preorder = []
    inorder = []
    postorder = []

    if root is None:
        return preorder, inorder, postorder

    stack = [(root, 1)]

    while stack:

        node, state = stack.pop()

        if state == 1:

            preorder.append(node.val)

            stack.append((node, 2))

            if node.left:
                stack.append((node.left, 1))

        elif state == 2:

            inorder.append(node.val)

            stack.append((node, 3))

            if node.right:
                stack.append((node.right, 1))

        else:

            postorder.append(node.val)

    return preorder, inorder, postorder
```

### Complexity

| Complexity | Value |
|---|---|
| Time | O(N) |
| Auxiliary stack | O(N) |
| Output | O(N) |

Each node is processed three times, which is still O(N).

---

## 9. Comparison of All Traversals

Using the same binary tree:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

| Traversal | Pattern | Output |
|---|---|---|
| Preorder | Root → Left → Right | `[1,2,4,5,3,6,7]` |
| Inorder | Left → Root → Right | `[4,2,5,1,6,3,7]` |
| Postorder | Left → Right → Root | `[4,5,2,6,7,3,1]` |
| Level Order | Level by Level | `[[1],[2,3],[4,5,6,7]]` |

### DFS vs BFS

| Feature | DFS | BFS |
|---|---|---|
| Full form | Depth First Search | Breadth First Search |
| Strategy | Explore deep first | Explore level by level |
| Common structures | Recursion / Stack | Queue |
| Tree traversals | Preorder, Inorder, Postorder | Level Order |

---

## 10. Important Python Concepts Used

### `deque`

```python
from collections import deque

queue = deque([1, 2, 3])

queue.popleft()
queue.append(4)
```

`deque` provides efficient operations at both ends.

### Stack — LIFO

```python
stack = []

stack.append(10)
stack.append(20)

stack.pop()  # 20
```

Last In, First Out.

### Queue — FIFO

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

queue.popleft()  # 10
```

First In, First Out.

### Recursive Base Case

```python
if root is None:
    return
```

Stops traversal when we reach a missing child.

### Shared Result List

```python
def preorder(root, ans):
    if root is None:
        return

    ans.append(root.val)

    preorder(root.left, ans)
    preorder(root.right, ans)

    return ans
```

$\color{#1f6feb}{\text{All recursive calls share the same list.}}$

Appending a value does not get undone when a recursive call returns.

---

## 11. Common Mistakes and Things to Remember

1. **Preorder:** Do not append after recursive calls. Append before them.
2. **Inorder:** Append between left and right recursive calls.
3. **Postorder:** Append only after both recursive calls.
4. **Iterative preorder:** Push right before left.
5. **Iterative inorder:** Keep moving left before popping from the stack.
6. **Iterative postorder:** Understand why the second stack reverses the first traversal's order.
7. **Level order:** Capture `level_size` before processing the current level.
8. **Queue:** Use `deque.popleft()`, not `list.pop(0)`.
9. **Empty tree:** Always handle `root is None`.
10. **Standalone files:** Each problem file should define its own `TreeNode` class and test construction.