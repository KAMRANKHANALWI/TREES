"""
Problem:
Find the path from the root to a given target node.

Pattern:
DFS + Recursion + Backtracking

Key Observation:
- Append the current node before exploring.
- Return True when the target is found.
- If neither subtree contains the target, pop the current node.
- Preserve the path once the target is found.

Approaches:
1. Recursive DFS with backtracking.

Complexity:
Time: O(N)
Space: O(H) auxiliary recursion/path space.
"""

# --------------------------------------------------
# Tree Node
# --------------------------------------------------


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# DFS + Backtracking
# --------------------------------------------------


def find_path(node, target, path):

    if node is None:
        return False

    # Include current node
    path.append(node.val)

    # Target found
    if node.val == target:
        return True

    # Search left subtree
    if find_path(node.left, target, path):
        return True

    # Search right subtree
    if find_path(node.right, target, path):
        return True

    # Target not found in either subtree
    path.pop()

    return False


# --------------------------------------------------
# Root to Node Path
# --------------------------------------------------


def root_to_node_path(root, target):

    path = []

    if find_path(root, target, path):
        return path

    return []


# --------------------------------------------------
# Build Sample Tree
# --------------------------------------------------


def build_sample_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)

    root.left.right.left = TreeNode(7)

    return root


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    root = build_sample_tree()

    print("Path to 7:", root_to_node_path(root, 7))
    print("Path to 6:", root_to_node_path(root, 6))
    print("Path to 4:", root_to_node_path(root, 4))
    print("Path to 100:", root_to_node_path(root, 100))

    print("Empty Tree:", root_to_node_path(None, 7))
