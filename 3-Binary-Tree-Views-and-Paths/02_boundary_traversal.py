"""
Problem:
    Given the root of a binary tree, return its boundary traversal
    in anti-clockwise direction.

    Boundary order:
    1. Root
    2. Left boundary (excluding leaf nodes)
    3. All leaf nodes (left to right)
    4. Right boundary (excluding leaf nodes, bottom to top)

Pattern:
    DFS + Boundary Traversal

Key Observation:
    Divide the boundary into three independent parts:
    - Left boundary
    - Leaf nodes
    - Right boundary

    Add the root separately to avoid duplicates.

Approaches:
    1. Traverse the left boundary iteratively.
    2. Collect leaves recursively using DFS.
    3. Traverse the right boundary iteratively and reverse it.

Complexity:
    - Time: O(N)
    - Auxiliary Space: O(H)
    - Output Space: O(N)
"""

# ============================================================
# Tree Node
# ============================================================


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
# Helper 1: Check Leaf Node
# ============================================================


def is_leaf(node):
    return node.left is None and node.right is None


# ============================================================
# Helper 2: Add Left Boundary
# ============================================================


def add_left_boundary(node, ans):

    # Start from the root's left child
    node = node.left

    while node:

        # Exclude leaf nodes
        if is_leaf(node):
            break

        ans.append(node.val)

        # Prefer left child
        if node.left:
            node = node.left
        else:
            node = node.right


# ============================================================
# Helper 3: Add All Leaf Nodes
# ============================================================


def add_leaves(node, ans):

    # Base case
    if node is None:
        return

    # If current node is a leaf
    if is_leaf(node):
        ans.append(node.val)
        return

    # Traverse left subtree first
    add_leaves(node.left, ans)

    # Then traverse right subtree
    add_leaves(node.right, ans)


# ============================================================
# Helper 4: Add Right Boundary
# ============================================================


def add_right_boundary(node, ans):

    # Start from the root's right child
    node = node.right

    temp = []

    while node:

        # Exclude leaf nodes
        if is_leaf(node):
            break

        temp.append(node.val)

        # Prefer right child
        if node.right:
            node = node.right
        else:
            node = node.left

    # Add boundary from bottom to top
    ans.extend(temp[::-1])


# ============================================================
# Main Function: Boundary Traversal
# ============================================================


def boundary_traversal(root):

    if root is None:
        return []

    # Special case: root itself is a leaf
    if is_leaf(root):
        return [root.val]

    ans = [root.val]

    # 1. Left boundary (top to bottom)
    add_left_boundary(root, ans)

    # 2. Leaf nodes (left to right)
    add_leaves(root, ans)

    # 3. Right boundary (bottom to top)
    add_right_boundary(root, ans)

    return ans


# ============================================================
# Build Test Trees
# ============================================================


def build_sample_tree():
    """
              1
            /   \
           2     3
          / \     \
         4   5     6
            / \     \
           8   9     7
    """

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(7)

    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    return root


# ============================================================
# Test Cases
# ============================================================

if __name__ == "__main__":

    # Test 1: General binary tree
    root = build_sample_tree()

    print("Boundary:", boundary_traversal(root))

    # Expected:
    # [1, 2, 4, 8, 9, 7, 6, 3]

    # Test 2: Empty tree
    print("Empty:", boundary_traversal(None))

    # Expected: []

    # Test 3: Single node
    single = TreeNode(10)

    print("Single:", boundary_traversal(single))

    # Expected: [10]

    # Test 4: Left-skewed tree
    left = TreeNode(1)
    left.left = TreeNode(2)
    left.left.left = TreeNode(3)
    left.left.left.left = TreeNode(4)

    print("Left Skewed:", boundary_traversal(left))

    # Expected: [1, 2, 3, 4]

    # Test 5: Right-skewed tree
    right = TreeNode(1)
    right.right = TreeNode(2)
    right.right.right = TreeNode(3)
    right.right.right.right = TreeNode(4)

    print("Right Skewed:", boundary_traversal(right))

    # Expected: [1, 4, 3, 2]
