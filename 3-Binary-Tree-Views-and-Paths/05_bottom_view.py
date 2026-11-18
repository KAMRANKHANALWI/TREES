
"""
Problem:
Return the bottom view of a binary tree.
The bottom view contains the bottommost node
at every horizontal distance, from left to right.

Pattern:
BFS + Horizontal Distance + Overwriting

Key Observation:
BFS visits nodes level by level.
Overwriting the value at each column ensures
that the deepest encountered node is retained.

Approaches:
1. BFS using a queue and dictionary.

Complexity:
Time: O(N log N)
Space: O(N)
"""

from collections import deque


# --------------------------------------------------
# Tree Node
# --------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# Bottom View of Binary Tree
# --------------------------------------------------

def bottom_view(root):

    if root is None:
        return []

    # Store the latest node encountered at each column
    bottom_view = {}

    # BFS queue: (node, column)
    queue = deque([(root, 0)])

    while queue:

        node, col = queue.popleft()

        # Always overwrite the existing value
        bottom_view[col] = node.val

        # Left child: column - 1
        if node.left:
            queue.append((node.left, col - 1))

        # Right child: column + 1
        if node.right:
            queue.append((node.right, col + 1))

    # Return nodes from leftmost to rightmost column
    return [bottom_view[col] for col in sorted(bottom_view)]


# --------------------------------------------------
# Build Sample Tree
# --------------------------------------------------

def build_sample_tree():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    root = build_sample_tree()

    print("Bottom View:", bottom_view(root))

    print("Empty Tree:", bottom_view(None))

    single = TreeNode(10)
    print("Single Node:", bottom_view(single))
