
"""
============================================================
04. DIAMETER OF BINARY TREE
============================================================

Problem:
Given the root of a binary tree, find its diameter.
The diameter is the longest path between any two nodes,
measured in number of edges.

Pattern:
DFS (Depth First Search) + Bottom-Up Recursion

Key Observation:
The longest path passing through a node is the sum
of the heights of its left and right subtrees.

Diameter Through Node:
left_height + right_height

Approaches:
1. Brute Force - Recalculate subtree heights.
2. Optimized DFS - Calculate height and diameter together.

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


def diameter_brute(root):

    if root is None:
        return 0

    # Calculate left and right subtree heights
    left_height = height(root.left)
    right_height = height(root.right)

    # Diameter passing through current node
    current_diameter = left_height + right_height

    # Calculate diameters of left and right subtrees
    left_diameter = diameter_brute(root.left)
    right_diameter = diameter_brute(root.right)

    # Return the maximum diameter
    return max(
        current_diameter,
        left_diameter,
        right_diameter
    )


# ============================================================
# APPROACH 2: OPTIMIZED DFS (BOTTOM-UP)
# ============================================================

def diameter_optimized(root):

    diameter = 0

    def height(node):
        nonlocal diameter

        # Base case
        if node is None:
            return 0

        # Get left and right subtree heights
        left_height = height(node.left)
        right_height = height(node.right)

        # Update maximum diameter
        diameter = max(
            diameter,
            left_height + right_height
        )

        # Return height to parent
        return 1 + max(left_height, right_height)

    height(root)

    return diameter


# ============================================================
# BUILD TEST TREES
# ============================================================

def build_tree_1():

    # Diameter passes through the root
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    return root


def build_tree_2():

    # Diameter exists inside the left subtree
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)

    return root


def build_tree_3():

    # Single-node tree
    return TreeNode(1)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    tree_1 = build_tree_1()
    tree_2 = build_tree_2()
    tree_3 = build_tree_3()

    print("Tree 1 - Brute:", diameter_brute(tree_1))
    print("Tree 1 - Optimized:", diameter_optimized(tree_1))

    print("Tree 2 - Brute:", diameter_brute(tree_2))
    print("Tree 2 - Optimized:", diameter_optimized(tree_2))

    print("Tree 3 - Brute:", diameter_brute(tree_3))
    print("Tree 3 - Optimized:", diameter_optimized(tree_3))
