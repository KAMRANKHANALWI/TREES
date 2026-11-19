
"""
Problem:
Find all nodes at a distance K from a given target node
in a binary tree.

Pattern:
Parent Mapping + Breadth First Search (BFS)

Key Observation:
A normal binary tree allows movement only towards children.
To move upwards, first store the parent of every node.

From the target, BFS can then explore:
    1. Left child
    2. Right child
    3. Parent

Use a visited set to avoid revisiting nodes.

Approaches:
1. Build parent mapping using BFS.
2. Perform BFS from the target for exactly K levels.

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


def build_parent_map(root):
    parent = {}
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            parent[node.left] = node
            queue.append(node.left)

        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    return parent


def nodes_at_distance_k(root, target, k):
    if root is None or target is None:
        return []

    # Step 1: Build parent mapping
    parent = build_parent_map(root)

    # Step 2: BFS starting from target
    queue = deque([target])
    visited = {target}

    distance = 0

    while queue and distance < k:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # Explore left child
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)

            # Explore right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)

            # Explore parent
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                queue.append(parent[node])

        distance += 1

    return [node.val for node in queue]


if __name__ == "__main__":

    # Construct Binary Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    # Target node = 5
    target = root.left.right

    print("Distance K = 0:", nodes_at_distance_k(root, target, 0))
    print("Distance K = 1:", nodes_at_distance_k(root, target, 1))
    print("Distance K = 2:", nodes_at_distance_k(root, target, 2))
    print("Distance K = 3:", nodes_at_distance_k(root, target, 3))

    # Empty Tree
    print("Empty Tree:", nodes_at_distance_k(None, None, 2))
