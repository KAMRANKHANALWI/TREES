
"""
Problem:
Find the maximum width of a binary tree.

Width of a level = position of rightmost node - position of leftmost node + 1.
Empty positions between nodes are also counted.

Pattern:
Level Order Traversal (BFS) + Positional Indexing

Key Observation:
Treat the tree like a complete binary tree for indexing.

For a node at index i:
    Left child  = 2 * i + 1
    Right child = 2 * i + 2

At each level:
    width = last_index - first_index + 1

Normalize indexes at every level to avoid unnecessarily
large integer values in a deep tree.

Approaches:
1. BFS with positional indexing and index normalization.

Complexity:
Time: O(N)
Space: O(N)
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maximum_width(root):
    if root is None:
        return 0

    queue = deque([(root, 0)])
    max_width = 0

    while queue:
        level_size = len(queue)

        # First index of the current level
        first_index = queue[0][1]

        first = last = 0

        for i in range(level_size):
            node, index = queue.popleft()

            # Normalize index to keep numbers small
            index -= first_index

            if i == 0:
                first = index

            if i == level_size - 1:
                last = index

            # Assign indexes to children
            if node.left:
                queue.append((node.left, 2 * index + 1))

            if node.right:
                queue.append((node.right, 2 * index + 2))

        # Calculate width of current level
        width = last - first + 1
        max_width = max(max_width, width)

    return max_width


if __name__ == "__main__":

    # Test Case 1: Normal Binary Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print("Maximum Width:", maximum_width(root))  # 4

    # Test Case 2: Complete Binary Tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)

    print("Complete Tree Width:", maximum_width(root2))  # 4

    # Test Case 3: Empty Tree
    print("Empty Tree:", maximum_width(None))  # 0

    # Test Case 4: Single Node
    root4 = TreeNode(10)
    print("Single Node:", maximum_width(root4))  # 1
