
"""
============================================================
06. PREORDER, INORDER AND POSTORDER IN ONE TRAVERSAL
============================================================

Problem:
Given the root of a binary tree, calculate preorder,
inorder and postorder traversals in a single traversal.

Pattern:
DFS + Stack + Node States

Key Observation:
Every node is processed at three different stages.

State 1: Preorder  -> Root
State 2: Inorder   -> Between Left and Right
State 3: Postorder -> After Left and Right

Approach:
Use a stack containing (node, state) pairs.

1. State 1:
   Append node to preorder.
   Push node with state 2.
   Push left child with state 1.

2. State 2:
   Append node to inorder.
   Push node with state 3.
   Push right child with state 1.

3. State 3:
   Append node to postorder.

Time Complexity:
O(N) - Every node is processed exactly three times.

Space Complexity:
O(N) - Auxiliary stack in the worst case.
Output: O(N) for all three traversal lists.

============================================================
"""

# ----------------------------------------------------------
# 1. TREE NODE
# ----------------------------------------------------------

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ----------------------------------------------------------
# 2. ALL THREE TRAVERSALS IN ONE ITERATION
# ----------------------------------------------------------

def all_traversals(root):
    preorder = []
    inorder = []
    postorder = []

    if root is None:
        return preorder, inorder, postorder

    # Stack stores (node, state)
    stack = [(root, 1)]

    while stack:

        node, state = stack.pop()

        # State 1: Preorder
        if state == 1:

            preorder.append(node.val)

            # Move current node to state 2
            stack.append((node, 2))

            # Process left subtree first
            if node.left:
                stack.append((node.left, 1))

        # State 2: Inorder
        elif state == 2:

            inorder.append(node.val)

            # Move current node to state 3
            stack.append((node, 3))

            # Process right subtree
            if node.right:
                stack.append((node.right, 1))

        # State 3: Postorder
        else:

            postorder.append(node.val)

    return preorder, inorder, postorder


# ----------------------------------------------------------
# 3. BUILD BINARY TREE
# ----------------------------------------------------------

def build_tree():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


# ----------------------------------------------------------
# 4. DRIVER CODE
# ----------------------------------------------------------

if __name__ == "__main__":

    root = build_tree()

    preorder, inorder, postorder = all_traversals(root)

    print("Preorder: ", preorder)
    print("Inorder:  ", inorder)
    print("Postorder:", postorder)
