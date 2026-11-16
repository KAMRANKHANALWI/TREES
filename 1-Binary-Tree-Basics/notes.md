# Binary Tree Notes

## Basics
- Each node has at most 2 children: `left`, `right`
- **Depth** = edges from root to node. **Height** = edges from node down to its deepest leaf
- **Leaf** = no children. **Subtree** = node + everything below it

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

**Types**
- **Full**: every node has 0 or 2 children
- **Complete**: all levels full except the last, which fills left to right (heaps use this)
- **Perfect**: all leaves on the same level, so nodes = 2^(h+1) − 1
- **Balanced**: height difference ≤ 1 at every node
- **Skewed**: one child per node, so it's basically a linked list and height = O(N)

Why height matters: every tree algorithm's space cost is O(H). Balanced gives H ≈ log N, skewed gives H = N.

---

## DFS: only the position of the "process" line changes

```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

| | Order | Output |
|---|---|---|
| Preorder | root, L, R | 1 2 4 5 3 6 7 |
| Inorder | L, root, R | 4 2 5 1 6 3 7 |
| Postorder | L, R, root | 4 5 2 6 7 3 1 |

```python
def dfs(root, ans):
    if not root: return
    # preorder: ans.append(root.val)
    dfs(root.left, ans)
    # inorder:  ans.append(root.val)
    dfs(root.right, ans)
    # postorder: ans.append(root.val)
```

BST inorder gives sorted order.

### Iterative

**Preorder**: stack, push **right first** so left pops first (LIFO)
```python
stack = [root]
while stack:
    node = stack.pop()
    ans.append(node.val)
    if node.right: stack.append(node.right)
    if node.left:  stack.append(node.left)
```

**Inorder**: go as far left as possible, then pop, process, go right
```python
stack, cur = [], root
while cur or stack:
    while cur:
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    ans.append(cur.val)
    cur = cur.right
```

**Postorder (2 stacks)**: gives root → right → left, and reversing that gives left → right → root
```python
s1, s2 = [root], []
while s1:
    node = s1.pop()
    s2.append(node)
    if node.left:  s1.append(node.left)
    if node.right: s1.append(node.right)
while s2:
    ans.append(s2.pop().val)
```

### All 3 in one pass
Stack of `(node, state)`. State = how many times we've visited the node. The 1st visit is preorder, the 2nd is inorder, the 3rd is postorder.

```python
stack = [(root, 1)]
while stack:
    node, state = stack.pop()
    if state == 1:
        pre.append(node.val)
        stack.append((node, 2))
        if node.left: stack.append((node.left, 1))
    elif state == 2:
        ino.append(node.val)
        stack.append((node, 3))
        if node.right: stack.append((node.right, 1))
    else:
        post.append(node.val)
```

Quick trace on node 2 (children 4, 5):
1. `(2,1)` pops → pre gets 2, push `(2,2)`, push `(4,1)`
2. 4 finishes completely
3. `(2,2)` pops → in gets 2, push `(2,3)`, push `(5,1)`
4. 5 finishes
5. `(2,3)` pops → post gets 2

---

## BFS (level order)
Queue (FIFO). **Grab `len(queue)` before the inner loop.** Children added during the loop belong to the next level, so the snapshot keeps levels separate.

```python
from collections import deque

def level_order(root):
    if not root: return []
    q, ans = deque([root]), []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(level)
    return ans
# [[1], [2, 3], [4, 5, 6, 7]]
```

---

## Complexity
All traversals are **O(N) time**. Auxiliary space (output not counted):

| | Space |
|---|---|
| Recursive DFS | O(H) (call stack) |
| Iterative pre / in | O(H) |
| Iterative post (2 stacks) | O(N) (stack2 holds every node) |
| Level order | O(N) (the widest level can be ~N/2) |
| All-in-one | O(H) |

> Note: all-in-one is O(H), not O(N). The stack only holds nodes on the current path, since right children are pushed only after the left subtree is fully done.

## Python quick ref
- Stack: `append()` / `pop()`
- Queue: `deque`, `append()` / `popleft()` (a list's `pop(0)` is O(N), so avoid it)