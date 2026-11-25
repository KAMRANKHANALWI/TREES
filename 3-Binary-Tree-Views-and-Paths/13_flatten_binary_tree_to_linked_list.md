# Flatten Binary Tree to Linked List

## 1. Understanding the Problem

Given the root of a binary tree, flatten it into a linked list **in-place**.

The flattened linked list must follow the same order as Preorder Traversal:

$$
Root \rightarrow Left \rightarrow Right
$$

The following conditions must be satisfied:

- The `left` pointer of every node must become `None`.
- The `right` pointer must point to the next node in preorder.
- We must rearrange the existing nodes without creating new nodes.

### Example

Original Binary Tree:

```text
          1
        /   \
       2     5
      / \     \
     3   4     6
```

Preorder Traversal:

$$
1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 6
$$

After flattening:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

The entire tree becomes a right-skewed linked list.

---

## 2. Key Observation

Preorder Traversal follows:

$$
Root \rightarrow Left \rightarrow Right
$$

Therefore, when we are at any node:

1. The current node must remain first.
2. Its left subtree must come next.
3. Its original right subtree must come after the entire left subtree.

The challenge is to rearrange the pointers without losing any part of the original tree.

Consider:

```text
          1
        /   \
       2     5
      / \     \
     3   4     6
```

At node `1`, we have:

- Left subtree: `2 → 3 → 4`
- Original right subtree: `5 → 6`

We want the final order:

$$
1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 6
$$

Therefore, we need to attach the original right subtree to the **rightmost node of the left subtree**.

In this example, the rightmost node of the left subtree is `4`.

After attaching the original right subtree:

```text
          1
           \
            2
           / \
          3   4
               \
                5
                 \
                  6
```

The left subtree comes first, and the original right subtree follows it.

---

## 3. Pointer Rearrangement at Every Node

We process the tree using a pointer called `curr`.

Whenever `curr` has a left child, we perform three operations.

### Step 1: Save the Original Right Subtree

```python
right_subtree = curr.right
```

We must save it before changing any pointers.

Otherwise, when we overwrite `curr.right`, we may lose access to the original right subtree.

### Step 2: Move the Left Subtree to the Right

```python
curr.right = curr.left
curr.left = None
```

The left subtree becomes the beginning of the flattened chain.

Before:

```text
      curr
     /    \
   left   right
```

After:

```text
      curr
        \
        left
```

The original right subtree has been temporarily saved in `right_subtree`.

### Step 3: Find the Rightmost Node

```python
temp = curr.right

while temp.right:
    temp = temp.right
```

We move through the right pointers until we reach the rightmost node of the moved subtree.

Why the rightmost node?

Because the entire left subtree must appear before the original right subtree in preorder.

### Step 4: Attach the Original Right Subtree

```python
temp.right = right_subtree
```

Now the original right subtree comes after the entire moved left subtree.

This preserves preorder.

---

## 4. Why We Use an Iterative Approach

We can flatten a binary tree using recursion, but this approach uses iteration and pointer manipulation.

We maintain:

```python
curr = root
```

At every node:

- If it has a left subtree, rearrange the pointers.
- If it does not have a left subtree, no rearrangement is needed.
- Move `curr` to the next node through `curr.right`.

```python
curr = curr.right
```

We continue until `curr` becomes `None`.

Since the tree is gradually transformed into a right-skewed structure, moving through the right pointers allows us to process every node.

---

## 5. Complete Dry Run

Consider the following tree:

```text
          1
        /   \
       2     5
      / \     \
     3   4     6
```

### Step 1: Process Node 1

Initially:

```python
curr = 1
```

Save the original right subtree:

```python
right_subtree = 5
```

Move the left subtree to the right:

```python
curr.right = curr.left
curr.left = None
```

Now:

```text
1
 \
  2
 / \
3   4

5
 \
  6
```

Find the rightmost node starting from node `2`.

```python
temp = 2

while temp.right:
    temp = temp.right
```

Movement:

$$
2 \rightarrow 4
$$

Node `4` is the rightmost node.

Attach node `5`:

```python
temp.right = right_subtree
```

The tree becomes:

```text
1
 \
  2
 / \
3   4
     \
      5
       \
        6
```

Move forward:

```python
curr = curr.right
```

Now `curr` is node `2`.

---

### Step 2: Process Node 2

Node `2` still has a left child, node `3`.

Save the original right subtree:

```python
right_subtree = 4
```

Move the left subtree to the right:

```python
curr.right = curr.left
curr.left = None
```

Now:

```text
2
 \
  3

4
 \
  5
   \
    6
```

Find the rightmost node of the moved subtree.

Node `3` has no right child, so it is already the rightmost node.

Attach node `4`:

```python
temp.right = right_subtree
```

The result:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

Move forward to node `3`.

---

### Step 3: Process Remaining Nodes

Nodes `3`, `4`, `5`, and `6` do not have left children.

Therefore, no pointer rearrangement is required.

We simply move:

$$
3 \rightarrow 4 \rightarrow 5 \rightarrow 6 \rightarrow None
$$

The algorithm terminates when `curr` becomes `None`.

### Final Result

```text
1 → 2 → 3 → 4 → 5 → 6 → None
```

This is exactly the preorder traversal of the original tree.

---

## 6. Complete Python Solution

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flatten(root):
    curr = root

    while curr:

        if curr.left:

            # Save the original right subtree
            right_subtree = curr.right

            # Move left subtree to the right
            curr.right = curr.left
            curr.left = None

            # Find the rightmost node of the moved subtree
            temp = curr.right

            while temp.right:
                temp = temp.right

            # Attach the original right subtree
            temp.right = right_subtree

        # Move to the next node
        curr = curr.right


# Print the flattened tree using right pointers
def print_flattened(root):
    curr = root

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.right

    print("None")


if __name__ == "__main__":

    # Test Case 1: Standard tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    flatten(root)

    print("Flattened Tree:")
    print_flattened(root)

    # Expected:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None


    # Test Case 2: Single node
    single = TreeNode(10)

    flatten(single)

    print("\nSingle Node:")
    print_flattened(single)

    # Expected:
    # 10 -> None


    # Test Case 3: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)

    flatten(left_skewed)

    print("\nLeft Skewed:")
    print_flattened(left_skewed)

    # Expected:
    # 1 -> 2 -> 3 -> None


    # Test Case 4: Right-skewed tree
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)

    flatten(right_skewed)

    print("\nRight Skewed:")
    print_flattened(right_skewed)

    # Expected:
    # 1 -> 2 -> 3 -> None


    # Test Case 5: Empty tree
    flatten(None)

    print("\nEmpty Tree:")
    print_flattened(None)

    # Expected:
    # None
```

---

## 7. Complexity Analysis

Let $N$ be the total number of nodes in the binary tree.

### Time Complexity: $O(N^2)$ in the worst case

The outer loop processes each node.

However, whenever a node has a left subtree, we traverse that subtree's right pointers to find its rightmost node.

In the worst case, this search may take $O(N)$ for a single node.

Therefore, the total time complexity can be:

$$
\boxed{O(N^2)}
$$

For example, when the tree contains long left-subtree chains, the rightmost-node search can repeatedly traverse many nodes.

### Space Complexity: $O(1)$

We use only a few pointers:

- `curr` — current node.
- `temp` — finding the rightmost node.
- `right_subtree` — temporarily storing the original right subtree.

No additional list, recursion stack, or data structure is required.

Therefore:

$$
\boxed{O(1)}
$$

---

## 8. Edge Cases

| Input | Expected Flattened Result | Explanation |
|---|---|---|
| Empty tree | `None` | Nothing to flatten |
| Single node | `10 → None` | Already flattened |
| Left-skewed tree | `1 → 2 → 3` | Left pointers become right pointers |
| Right-skewed tree | `1 → 2 → 3` | Already follows required structure |
| Normal binary tree | Preorder sequence | Rearrange pointers to preserve preorder |

---

## 9. Final Takeaway

The main challenge in this problem is not traversal. It is **preserving the original subtree connections while rearranging pointers**.

At every node:

1. Save the original right subtree.
2. Move the left subtree to the right.
3. Set the left pointer to `None`.
4. Find the rightmost node of the moved subtree.
5. Attach the original right subtree.
6. Move to the next node.

The most important observation:

\color{#1f6feb}{The original right subtree must be attached to the rightmost node of the moved left subtree so that preorder order is preserved.}

The final structure follows:

$$
Root \rightarrow Left \rightarrow Right
$$

but is represented entirely through right pointers.

**Pattern:** In-place Tree Modification + Preorder Pointer Rearrangement.