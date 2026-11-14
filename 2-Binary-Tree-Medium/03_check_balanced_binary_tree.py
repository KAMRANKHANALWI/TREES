"""
============================================================
03. CHECK BALANCED BINARY TREE
============================================================

Problem:
Given the root of a binary tree, check whether it is
height-balanced.

Pattern:
DFS (Depth First Search) + Recursion

Key Observation:
A tree is balanced if, at every node, the difference
between left and right subtree heights is at most 1.

Balance Condition:
abs(left_height - right_height) <= 1

Approaches:
1. Brute Force - Recalculate subtree heights.
2. Optimized DFS - Return height or -1.

Time Complexity:
Brute Force: O(N^2) worst case.
Optimized: O(N) - Each node is visited once.

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
# APPROACH 1: BRUTE FORCE
# ============================================================


def height(root):

    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


def is_balanced_brute(root):

    # Base case
    if root is None:
        return True

    # Calculate left and right subtree heights
    left_height = height(root.left)
    right_height = height(root.right)

    # Check balance condition at current node
    if abs(left_height - right_height) > 1:
        return False

    # Check both subtrees
    return is_balanced_brute(root.left) and is_balanced_brute(root.right)


# ============================================================
# APPROACH 2: OPTIMIZED DFS (BOTTOM-UP)
# ============================================================


def is_balanced(root):

    def check_height(node):

        # Base case: Empty subtree has height 0
        if node is None:
            return 0

        # Get left subtree height
        left_height = check_height(node.left)

        # Propagate unbalanced signal
        if left_height == -1:
            return -1

        # Get right subtree height
        right_height = check_height(node.right)

        # Propagate unbalanced signal
        if right_height == -1:
            return -1

        # Check balance condition
        if abs(left_height - right_height) > 1:
            return -1

        # Return actual height if balanced
        return 1 + max(left_height, right_height)

    # True if balanced, False otherwise
    return check_height(root) != -1


# ============================================================
# BUILD TEST TREES
# ============================================================


def build_balanced_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    return root


def build_unbalanced_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)

    return root


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    balanced_tree = build_balanced_tree()
    unbalanced_tree = build_unbalanced_tree()

    print("Balanced Tree (Brute):", is_balanced_brute(balanced_tree))

    print("Balanced Tree (Optimized):", is_balanced(balanced_tree))

    print("Unbalanced Tree (Brute):", is_balanced_brute(unbalanced_tree))

    print("Unbalanced Tree (Optimized):", is_balanced(unbalanced_tree))
