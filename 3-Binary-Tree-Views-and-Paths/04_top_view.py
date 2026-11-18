
"""
Problem:
Return the top view of a binary tree.
The top view contains the first visible node
at every horizontal distance, from left to right.

Pattern:
BFS + Horizontal Distance + First Encounter

Key Observation:
BFS visits nodes level by level.
Therefore, the first node encountered at a
horizontal distance is the topmost visible node.

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
# Top View of Binary Tree
# --------------------------------------------------

def top_view(root):

    if root is None:
        return []

    # Store the first node encountered at each column
    top_view = {}

    # BFS queue: (node, column)
    queue = deque([(root, 0)])

    while queue:

        node, col = queue.popleft()

        # Store only the first node at this column
        if col not in top_view:
            top_view[col] = node.val

        # Left child: column - 1
        if node.left:
            queue.append((node.left, col - 1))

        # Right child: column + 1
        if node.right:
            queue.append((node.right, col + 1))

    # Return nodes from leftmost to rightmost column
    return [top_view[col] for col in sorted(top_view)]


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

    print("Top View:", top_view(root))

    print("Empty Tree:", top_view(None))

    single = TreeNode(10)
    print("Single Node:", top_view(single))

