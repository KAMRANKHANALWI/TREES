
"""
Problem:
Return the left and right views of a binary tree.

Pattern:
BFS + Level Order Traversal

Key Observation:
- Left View: First node at every level.
- Right View: Last node at every level.
- BFS processes nodes level by level.

Approaches:
1. BFS using a queue and level size.

Complexity:
Time: O(N)
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
# Left View
# --------------------------------------------------

def left_view(root):

    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:

        level_size = len(queue)

        for i in range(level_size):

            node = queue.popleft()

            # First node of every level
            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result


# --------------------------------------------------
# Right View
# --------------------------------------------------

def right_view(root):

    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:

        level_size = len(queue)

        for i in range(level_size):

            node = queue.popleft()

            # Last node of every level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result


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

    print("Left View:", left_view(root))
    print("Right View:", right_view(root))

    print("Empty Tree - Left:", left_view(None))
    print("Empty Tree - Right:", right_view(None))

    single = TreeNode(10)

    print("Single Node - Left:", left_view(single))
    print("Single Node - Right:", right_view(single))
