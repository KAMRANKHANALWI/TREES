# Binary Tree Medium Notes

Almost everything here is one idea: **recurse on the children, combine at the node**. The only thing that changes is what you return and what you do with it.

| # | Problem | Pattern |
|---|---|---|
| 01 | Maximum Depth | return height |
| 02 | Identical Trees | walk two trees together |
| 03 | Balanced Tree | return height or `-1` |
| 04 | Diameter | return height, track best on the side |
| 05 | Max Path Sum | return one branch, track best on the side |
| 06 | Symmetric Tree | walk two trees, cross-compare |
| 07 | Children Sum | check every non-leaf |

---

## 01. Maximum Depth
Height of a node = 1 + the taller child. Empty tree = 0.

```python
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

O(N) time, O(H) space. This is the base template for 03 and 04.

---

## 02. Identical Trees
Walk both trees at the same time, same direction.

```python
def is_same(p, q):
    if not p or not q:
        return p is q          # both None -> True, only one None -> False
    return (p.val == q.val
            and is_same(p.left, q.left)
            and is_same(p.right, q.right))
```

O(N) time, O(H) space.

---

## 03. Balanced Binary Tree
**Brute force**: call `height()` at every node and compare. Height itself is O(N), and you call it N times, so **O(N²)**.

**Fix**: compute height and check balance in the same pass. Return `-1` as a "this subtree is already broken" signal, and pass it straight up.

```python
def check(node):
    if not node: return 0
    l = check(node.left)
    if l == -1: return -1
    r = check(node.right)
    if r == -1: return -1
    if abs(l - r) > 1: return -1
    return 1 + max(l, r)

is_balanced = check(root) != -1
```

O(N) time, O(H) space. `-1` can never be a real height, which is why it works as a flag.

---

## 04. Diameter
Longest path between any two nodes, counted in **edges**. It may not pass through the root.

At any node, the longest path *through* it = `left_height + right_height`. So visit every node, and keep the best.

```python
def diameter_of_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node: return 0
        l = height(node.left)
        r = height(node.right)
        diameter = max(diameter, l + r)    # path bending through this node
        return 1 + max(l, r)               # parent can only extend ONE side

    height(root)
    return diameter
```

Brute force is O(N²) (height at every node). This is O(N) time, O(H) space.

Two different numbers at each node:
- **update global** with both sides (path bends here)
- **return to parent** with one side (a path going up can't fork)

This same split is the whole trick in 05.

---

## 05. Maximum Path Sum
Same shape as diameter, but with values instead of lengths. Path can start and end anywhere, and can't branch.

Negative child? Don't take it: `max(0, gain)`.

```python
def max_path_sum(root):
    max_sum = float("-inf")     # not 0, tree could be all negative

    def gain(node):
        nonlocal max_sum
        if not node: return 0
        l = max(0, gain(node.left))
        r = max(0, gain(node.right))
        max_sum = max(max_sum, node.val + l + r)   # path bends here
        return node.val + max(l, r)                # parent gets one side only

    gain(root)
    return max_sum
```

O(N) time, O(H) space.

| Purpose | Formula |
|---|---|
| Update global best | `val + l + r` |
| Return to parent | `val + max(l, r)` |

---

## 06. Symmetric Tree
Same as identical trees, but you cross the sides: outer pairs with outer, inner with inner.

```python
def is_symmetric(root):
    def mirror(a, b):
        if not a or not b:
            return a is b
        return (a.val == b.val
                and mirror(a.left, b.right)
                and mirror(a.right, b.left))
    return mirror(root.left, root.right) if root else True
```

| Identical | Symmetric |
|---|---|
| left ↔ left | left ↔ right |
| right ↔ right | right ↔ left |

O(N) time, O(H) space.

---

## 07. Children Sum Property
Every non-leaf must equal `left.val + right.val`. Missing child counts as 0. Leaves pass automatically.

```python
def children_sum(root):
    if not root: return True
    if not root.left and not root.right: return True   # leaf

    child_sum = 0
    if root.left:  child_sum += root.left.val
    if root.right: child_sum += root.right.val

    if root.val != child_sum: return False
    return children_sum(root.left) and children_sum(root.right)
```

O(N) time, O(H) space.

---

## Cheat sheet

| Problem | Return | Side effect |
|---|---|---|
| Max Depth | height | none |
| Balanced | height or `-1` | none |
| Diameter | height | `l + r` into global |
| Max Path Sum | best single-branch gain | `val + l + r` into global |
| Identical / Symmetric | bool | none |

## Complexity
N = nodes, H = height. Space is O(H) everywhere (recursion stack).

| Problem | Time |
|---|---|
| Max Depth | O(N) |
| Identical | O(N) |
| Balanced | O(N²) brute, O(N) optimized |
| Diameter | O(N²) brute, O(N) optimized |
| Max Path Sum | O(N) |
| Symmetric | O(N) |
| Children Sum | O(N) |

## Python bits
- `nonlocal`: lets the inner function update the outer variable (`diameter`, `max_sum`)
- `float("-inf")`: safe starting point when answers can be negative
- `p is q` in the None check: a compact way to say "both None"