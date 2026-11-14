
"""
============================================================
01. MAXIMUM DEPTH OF BINARY TREE
============================================================

Problem:
Given the root of a binary tree, find its maximum depth.

Pattern:
DFS (Depth First Search) + Recursion

Key Observation:
The maximum depth of a node depends on the maximum
depth of its left and right subtrees.

Formula:
Depth(root) = 1 + max(left_depth, right_depth)

Approaches:
1. Recursive DFS (Bottom-Up)
2. Iterative BFS using Queue

Time Complexity:
O(N) - Every node is visited exactly once.

Space Complexity:
Recursive: O(H) auxiliary recursion stack.
BFS: O(W) auxiliary queue space.

Where:
N = Number of nodes
H = Height of the tree
W = Maximum width of the tree

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
# 2. RECURSIVE APPROACH - DFS
# ----------------------------------------------------------

def max_depth(root):

    # Base Case
    if root is None:
        return 0

    # Calculate left subtree depth
    left_depth = max_depth(root.left)

    # Calculate right subtree depth
    right_depth = max_depth(root.right)

    # Return current node depth
    return 1 + max(left_depth, right_depth)


# ----------------------------------------------------------
# 3. ITERATIVE APPROACH - BFS
# ----------------------------------------------------------

def max_depth_bfs(root):

    if root is None:
        return 0

    queue = deque([root])
    depth = 0

    while queue:

        # Number of nodes at current level
        level_size = len(queue)

        # Move to next level
        depth += 1

        for _ in range(level_size):

            node = queue.popleft()

            # Add left child
            if node.left:
                queue.append(node.left)

            # Add right child
            if node.right:
                queue.append(node.right)

    return depth


# ----------------------------------------------------------
# 4. BUILD BINARY TREE
# ----------------------------------------------------------

def build_tree():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.left.left.left = TreeNode(6)

    return root


# ----------------------------------------------------------
# 5. DRIVER CODE
# ----------------------------------------------------------

if __name__ == "__main__":

    root = build_tree()

    recursive_result = max_depth(root)
    iterative_result = max_depth_bfs(root)

    print("Maximum Depth (Recursive):", recursive_result)
    print("Maximum Depth (BFS):", iterative_result)
