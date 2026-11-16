"""
============================================================
06. SYMMETRIC BINARY TREE
============================================================

Problem:
Given the root of a binary tree, check whether it is
symmetric around its center.

Pattern:
DFS (Depth First Search) + Recursion

Key Observation:
A tree is symmetric if its left and right subtrees
are mirror images of each other.

Mirror Comparison:
1. Left child of first subtree == Right child of second.
2. Right child of first subtree == Left child of second.

Approaches:
1. Recursive DFS (Mirror Comparison)

Time Complexity:
O(N) - Each node is visited at most once.

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
# APPROACH 1: RECURSIVE DFS (MIRROR COMPARISON)
# ============================================================


def is_symmetric(root):

    def is_mirror(left, right):

        # Case 1: Both nodes are empty
        if left is None and right is None:
            return True

        # Case 2: Only one node is empty
        if left is None or right is None:
            return False

        # Case 3: Node values must match
        if left.val != right.val:
            return False

        # Compare opposite children
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    # Empty tree is symmetric
    if root is None:
        return True

    # Compare left and right subtrees
    return is_mirror(root.left, root.right)


# ============================================================
# BUILD TEST TREES
# ============================================================


def build_symmetric_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)

    return root


def build_asymmetric_value_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.right.right = TreeNode(4)

    return root


def build_asymmetric_structure_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)

    return root


def build_single_node_tree():

    return TreeNode(1)


def build_empty_tree():

    return None


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    test_cases = [
        ("Symmetric Tree", build_symmetric_tree(), True),
        ("Different Node Values", build_asymmetric_value_tree(), False),
        ("Different Structure", build_asymmetric_structure_tree(), False),
        ("Single Node", build_single_node_tree(), True),
        ("Empty Tree", build_empty_tree(), True),
    ]

    for name, root, expected in test_cases:

        result = is_symmetric(root)

        print(f"{name}: {result} | Expected: {expected}")
