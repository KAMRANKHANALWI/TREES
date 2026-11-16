"""
============================================================
07. CHILDREN SUM PROPERTY
============================================================

Problem:
Given the root of a binary tree, check whether it follows
the Children Sum Property.

For every non-leaf node:
Node.val = Left.val + Right.val

A missing child is considered to have value 0.
Leaf nodes automatically satisfy the property.

Pattern:
DFS (Depth First Search) + Recursion

Key Observation:
Check the children sum condition at every non-leaf node.
Both left and right subtrees must also satisfy the property.

Approaches:
1. Recursive DFS

Time Complexity:
O(N) - Every node is visited once.

Space Complexity:
O(H) - Recursive call stack.

Where:
N = Number of nodes
H = Height of the tree

============================================================
"""

# ============================================================
# TREE NODE
# ============================================================


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
# APPROACH 1: RECURSIVE DFS
# ============================================================


def is_children_sum(root):

    # Case 1: Empty tree
    if root is None:
        return True

    # Case 2: Leaf node
    if root.left is None and root.right is None:
        return True

    # Calculate sum of existing children
    child_sum = 0

    if root.left:
        child_sum += root.left.val

    if root.right:
        child_sum += root.right.val

    # Check current node
    if root.val != child_sum:
        return False

    # Check left and right subtrees
    return is_children_sum(root.left) and is_children_sum(root.right)


# ============================================================
# BUILD TEST TREES
# ============================================================


def build_valid_tree():

    # 10 = 4 + 6
    # 4 = 2 + 2

    root = TreeNode(10)

    root.left = TreeNode(4)
    root.right = TreeNode(6)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(2)

    return root


def build_invalid_tree():

    # Root satisfies the property.
    # Node 4 violates it: 4 != 1 + 2

    root = TreeNode(10)

    root.left = TreeNode(4)
    root.right = TreeNode(6)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    return root


def build_single_child_tree():

    # 5 = 5 + 0

    root = TreeNode(5)
    root.left = TreeNode(5)

    return root


def build_single_node_tree():

    return TreeNode(5)


def build_empty_tree():

    return None


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    test_cases = [
        ("Valid Tree", build_valid_tree(), True),
        ("Invalid Tree", build_invalid_tree(), False),
        ("Single Child Tree", build_single_child_tree(), True),
        ("Single Node Tree", build_single_node_tree(), True),
        ("Empty Tree", build_empty_tree(), True),
    ]

    for name, root, expected in test_cases:

        result = is_children_sum(root)

        print(f"{name}: {result} | Expected: {expected}")
