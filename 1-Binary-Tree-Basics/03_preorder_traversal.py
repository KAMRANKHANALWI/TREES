
"""
============================================================
03. PREORDER TRAVERSAL
============================================================

Problem:
Given the root of a binary tree, return the preorder
traversal of its nodes.

Pattern:
DFS (Depth First Search)

Traversal:
Root -> Left -> Right

Key Observation:
Process the current node immediately, before visiting
its left and right subtrees.

Approaches:
1. Recursive DFS
2. Iterative DFS using Stack

Time Complexity:
O(N) - Every node is visited exactly once.

Space Complexity:
Recursive: O(H) auxiliary recursion stack.
Iterative: O(H) auxiliary stack in the typical analysis.
Output: O(N).

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
# 2. RECURSIVE APPROACH
# ----------------------------------------------------------

def preorder_recursive(root, ans):
    if root is None:
        return

    # Step 1: Process current node
    ans.append(root.val)

    # Step 2: Traverse left subtree
    preorder_recursive(root.left, ans)

    # Step 3: Traverse right subtree
    preorder_recursive(root.right, ans)

    return ans


# ----------------------------------------------------------
# 3. ITERATIVE APPROACH
# ----------------------------------------------------------

def preorder_iterative(root):
    if root is None:
        return []

    stack = [root]
    ans = []

    while stack:
        node = stack.pop()

        # Process current node
        ans.append(node.val)

        # Push right first
        if node.right:
            stack.append(node.right)

        # Push left second
        if node.left:
            stack.append(node.left)

    return ans


# ----------------------------------------------------------
# 4. BUILD BINARY TREE
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
# 5. DRIVER CODE
# ----------------------------------------------------------

if __name__ == "__main__":
    root = build_tree()

    recursive_result = preorder_recursive(root, [])
    iterative_result = preorder_iterative(root)

    print("Recursive:", recursive_result)
    print("Iterative:", iterative_result)
