"""
============================================================
05. MAXIMUM PATH SUM IN BINARY TREE
============================================================

Problem:
Given the root of a binary tree, find the maximum sum
of values along any valid path.

A path can start and end at any nodes, but cannot branch
or visit the same node more than once.

Pattern:
DFS (Depth First Search) + Bottom-Up Recursion

Key Observation:
At every node, calculate the maximum path passing through it
using both left and right gains.

Ignore negative child contributions using max(0, gain).

Global Maximum:
node.val + left_gain + right_gain

Return to Parent:
node.val + max(left_gain, right_gain)

Approaches:
1. Recursive reference approach - Enumerate possible paths.
2. Optimized DFS - Calculate maximum gain in one traversal.

Time Complexity:
Reference: O(N^2) with the implementation below.
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
# APPROACH 1: BRUTE FORCE / REFERENCE
# ============================================================


def max_gain_from_node(node):
    """
    Returns the maximum downward path sum starting at node.

    A path can continue through only one child.
    Negative contributions are ignored.
    """

    if node is None:
        return 0

    left_gain = max(0, max_gain_from_node(node.left))
    right_gain = max(0, max_gain_from_node(node.right))

    return node.val + max(left_gain, right_gain)


def max_path_sum_brute(root):
    """
    Try every node as the highest point (turning point)
    of a candidate path.

    For each node:
    1. Calculate its left downward gain.
    2. Calculate its right downward gain.
    3. Combine both gains through the current node.
    4. Recursively check the remaining nodes.
    """

    if root is None:
        return 0

    # Maximum path passing through current node
    left_gain = max(0, max_gain_from_node(root.left))
    right_gain = max(0, max_gain_from_node(root.right))

    current_sum = root.val + left_gain + right_gain

    # Check paths inside left and right subtrees
    left_max = max_path_sum_brute(root.left)
    right_max = max_path_sum_brute(root.right)

    return max(current_sum, left_max, right_max)


# ============================================================
# APPROACH 2: OPTIMIZED DFS (BOTTOM-UP)
# ============================================================


def max_path_sum(root):

    # Start with negative infinity because all values
    # in the tree could be negative.
    max_sum = float("-inf")

    def max_gain(node):
        nonlocal max_sum

        # Base case
        if node is None:
            return 0

        # Get maximum positive gains from both subtrees
        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))

        # Maximum path passing through current node
        current_sum = node.val + left_gain + right_gain

        # Update global maximum
        max_sum = max(max_sum, current_sum)

        # Return only one branch to the parent
        return node.val + max(left_gain, right_gain)

    # Calculate gains for the entire tree
    max_gain(root)

    return max_sum


# ============================================================
# BUILD TEST TREES
# ============================================================


def build_tree_1():

    # Maximum path: 15 -> 20 -> 7
    # Expected sum: 42

    root = TreeNode(-10)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


def build_tree_2():

    # Maximum path: 4 -> 2 -> 5
    # Expected sum: 11

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    return root


def build_tree_3():

    # All negative values
    # Maximum path: -3
    # Expected sum: -3

    root = TreeNode(-10)

    root.left = TreeNode(-2)
    root.right = TreeNode(-3)

    return root


def build_tree_4():

    # Single-node tree
    # Expected sum: 5

    return TreeNode(5)


def build_tree_5():

    # Maximum path is entirely inside the left subtree.
    # Path: 15 -> 20 -> 7
    # Expected sum: 42

    root = TreeNode(-10)

    root.left = TreeNode(20)
    root.right = TreeNode(-5)

    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)

    return root


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    test_cases = [
        ("Mixed positive and negative", build_tree_1(), 42),
        ("Maximum path through root", build_tree_2(), 11),
        ("All negative values", build_tree_3(), -2),
        ("Single node", build_tree_4(), 5),
        ("Maximum path inside subtree", build_tree_5(), 42),
    ]

    for name, root, expected in test_cases:

        brute_result = max_path_sum_brute(root)
        optimized_result = max_path_sum(root)

        print(f"\n{name}")
        print("Expected:", expected)
        print("Brute Force:", brute_result)
        print("Optimized:", optimized_result)
        print("Passed:", brute_result == expected and optimized_result == expected)
