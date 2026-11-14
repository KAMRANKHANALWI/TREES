"""
============================================================
02. CHECK IDENTICAL TREES
============================================================

Problem:
Given the roots of two binary trees, check whether they
are identical in both structure and node values.

Pattern:
DFS (Depth First Search) + Recursion

Key Observation:
Two trees are identical if:
1. Both corresponding nodes are None, OR
2. Both nodes exist, have equal values, and their
   left and right subtrees are identical.

Approaches:
1. Recursive DFS

Time Complexity:
O(N) - Each corresponding node pair is checked at most once.
N = Number of nodes (for equal trees).

Space Complexity:
O(H) - Recursive call stack.
H = Height of the trees.

============================================================
"""

# ============================================================
# TREE NODE
# ============================================================


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
# APPROACH 1: RECURSIVE DFS
# ============================================================


def is_same_tree(p, q):

    # Case 1: Both nodes are empty
    if p is None and q is None:
        return True

    # Case 2: Only one node is empty
    if p is None or q is None:
        return False

    # Case 3: Node values are different
    if p.val != q.val:
        return False

    # Compare left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# ============================================================
# BUILD TEST TREES
# ============================================================


def build_tree_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def build_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def build_tree_different_value():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    return root


def build_tree_different_structure():
    root = TreeNode(1)
    root.right = TreeNode(2)
    return root


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    tree_1 = build_tree_1()
    tree_2 = build_tree_2()

    tree_3 = build_tree_different_value()
    tree_4 = build_tree_different_structure()

    print("Identical Trees:", is_same_tree(tree_1, tree_2))
    print("Different Values:", is_same_tree(tree_1, tree_3))
    print("Different Structure:", is_same_tree(tree_1, tree_4))
