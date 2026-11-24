r"""
Problem:
Count the total number of nodes in a Complete Binary Tree.

Complete Binary Tree:
All levels are full, except maybe the last one.
The last level fills from left to right, with no gaps.

Complete (no gaps on the last level):

        1
       / \
      2   3
     / \  /
    4  5 6

Not complete (2 has a right child but no left child):

        1
       / \
      2   3
       \
        5

Pattern:
Binary Tree Recursion + Height Calculation

Key Observation:
If the leftmost and rightmost heights of a subtree
are equal, that subtree is perfect.

Number of nodes in a perfect binary tree:
2^H - 1

Approach:
1. Calculate leftmost height.
2. Calculate rightmost height.
3. If equal, return 2^H - 1.
4. Otherwise, recursively count both subtrees.

Complexity:
Time: O(log^2 N)
Space: O(log N)
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def left_height(node):
    height = 0

    while node:
        height += 1
        node = node.left

    return height


def right_height(node):
    height = 0

    while node:
        height += 1
        node = node.right

    return height


def count_nodes(root):
    if root is None:
        return 0

    lh = left_height(root)
    rh = right_height(root)

    # Perfect binary subtree
    if lh == rh:
        return (1 << lh) - 1

    # Count root + left subtree + right subtree
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    print("Total Nodes:", count_nodes(root))
