
"""
Problem:
    Given the root of a binary tree, return its level-order traversal
    in zigzag order.

    Alternate the direction at every level:
    Level 0 -> Left to Right
    Level 1 -> Right to Left
    Level 2 -> Left to Right
    ...

Pattern:
    BFS (Level Order Traversal) + Direction Toggle

Key Observation:
    The queue always processes nodes in normal BFS order.
    Only the position where values are stored changes.

Approaches:
    1. Simple:
       Perform normal BFS and reverse alternate levels.

    2. Optimized:
       Use an index to directly place values in zigzag order.
       - Left to Right: index = i
       - Right to Left: index = size - 1 - i

Complexity:
    Both approaches:
    - Time: O(N)
    - Auxiliary Space: O(N) worst case
"""

from collections import deque


# ============================================================
# Tree Node
# ============================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
# Approach 1: BFS + Reverse Alternate Levels
# ============================================================

def zigzag_traversal_brute(root):
    """
    Perform normal BFS and reverse every alternate level.
    """

    if root is None:
        return []

    queue = deque([root])
    ans = []

    left_to_right = True

    while queue:

        size = len(queue)
        level = []

        # Process all nodes at the current level
        for _ in range(size):

            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        # Reverse alternate levels
        if not left_to_right:
            level.reverse()

        ans.append(level)

        # Toggle direction for next level
        left_to_right = not left_to_right

    return ans


# ============================================================
# Approach 2: BFS + Direct Index Placement
# ============================================================

def zigzag_traversal(root):
    """
    Store each node directly at its correct zigzag index.
    Avoid reversing the level afterwards.
    """

    if root is None:
        return []

    queue = deque([root])
    ans = []

    left_to_right = True

    while queue:

        size = len(queue)

        # Allocate positions for the current level
        level = [0] * size

        # Process all nodes at the current level
        for i in range(size):

            node = queue.popleft()

            # Decide the correct position
            if left_to_right:
                index = i
            else:
                index = size - 1 - i

            level[index] = node.val

            # Always enqueue children left to right
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        ans.append(level)

        # Toggle direction for next level
        left_to_right = not left_to_right

    return ans


# ============================================================
# Build Test Trees
# ============================================================

def build_sample_tree():
    """
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
    """

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


# ============================================================
# Test Cases
# ============================================================

if __name__ == "__main__":

    # Test 1: Complete binary tree
    root = build_sample_tree()

    print("Brute:", zigzag_traversal_brute(root))
    print("Optimal:", zigzag_traversal(root))

    # Expected:
    # [[1], [3, 2], [4, 5, 6, 7]]

    # Test 2: Empty tree
    print("Empty:", zigzag_traversal(None))

    # Expected: []

    # Test 3: Single node
    single = TreeNode(10)

    print("Single:", zigzag_traversal(single))

    # Expected: [[10]]

    # Test 4: Left-skewed tree
    skewed = TreeNode(1)
    skewed.left = TreeNode(2)
    skewed.left.left = TreeNode(3)
    skewed.left.left.left = TreeNode(4)

    print("Skewed:", zigzag_traversal(skewed))

    # Expected: [[1], [2], [3], [4]]
