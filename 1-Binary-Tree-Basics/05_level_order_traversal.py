
"""
============================================================
05. LEVEL ORDER TRAVERSAL
============================================================

Problem:
Given the root of a binary tree, return its level order
traversal, visiting nodes level by level from left to right.

Pattern:
BFS (Breadth First Search)

Key Observation:
Use a Queue (FIFO) to process nodes in the order they
are discovered.

Approach:
1. Initialize a queue with the root.
2. Process all nodes belonging to the current level.
3. Add their children to the queue.
4. Store each completed level in the answer.

Time Complexity:
O(N) - Every node is visited exactly once.

Space Complexity:
O(N) - Queue can hold up to O(N) nodes.
Output: O(N).

============================================================
"""

from collections import deque


# ----------------------------------------------------------
# 1. TREE NODE
# ----------------------------------------------------------

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ----------------------------------------------------------
# 2. LEVEL ORDER TRAVERSAL - BFS
# ----------------------------------------------------------

def level_order(root):
    if root is None:
        return []

    queue = deque([root])
    ans = []

    while queue:

        # Number of nodes at current level
        level_size = len(queue)

        level = []

        for _ in range(level_size):

            node = queue.popleft()

            # Process current node
            level.append(node.val)

            # Add children for next level
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        # Store completed level
        ans.append(level)

    return ans


# ----------------------------------------------------------
# 3. BUILD BINARY TREE
# ----------------------------------------------------------

def build_tree():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


# ----------------------------------------------------------
# 4. DRIVER CODE
# ----------------------------------------------------------

if __name__ == "__main__":
    root = build_tree()

    result = level_order(root)

    print("Level Order:", result)
