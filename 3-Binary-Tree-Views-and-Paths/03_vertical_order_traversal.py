
"""
Problem:
Return the vertical order traversal of a binary tree.
Nodes are ordered by column, then row, and by value
when multiple nodes share the same coordinates.

Pattern:
BFS + Coordinate Mapping + Nested Dictionary

Key Observation:
- Root starts at (row=0, col=0).
- Left child: (row+1, col-1).
- Right child: (row+1, col+1).
- Store values using nodes[col][row].
- Sort columns, rows, and values.

Approaches:
1. BFS with nested defaultdict.

Complexity:
Time: O(N log N) approximately, due to sorting.
Space: O(N).
"""

from collections import defaultdict, deque


# --------------------------------------------------
# Tree Node
# --------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# Vertical Order Traversal
# --------------------------------------------------

def vertical_traversal(root):

    if root is None:
        return []

    # Store: column -> row -> list of node values
    nodes = defaultdict(lambda: defaultdict(list))

    # BFS queue: (node, row, column)
    queue = deque([(root, 0, 0)])

    # Step 1: Traverse the tree using BFS
    while queue:

        node, row, col = queue.popleft()

        # Store node value at its coordinates
        nodes[col][row].append(node.val)

        # Left child: row + 1, column - 1
        if node.left:
            queue.append((node.left, row + 1, col - 1))

        # Right child: row + 1, column + 1
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    # Step 2: Build the final result
    result = []

    # Process columns from left to right
    for col in sorted(nodes):

        column = []

        # Process rows from top to bottom
        for row in sorted(nodes[col]):

            # Sort values sharing the same coordinates
            values = sorted(nodes[col][row])

            column.extend(values)

        result.append(column)

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

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    root = build_sample_tree()

    print("Vertical Traversal:", vertical_traversal(root))

    print("Empty Tree:", vertical_traversal(None))

    single = TreeNode(10)
    print("Single Node:", vertical_traversal(single))
