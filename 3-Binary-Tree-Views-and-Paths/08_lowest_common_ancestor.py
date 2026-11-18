
"""
Problem:
Find the Lowest Common Ancestor (LCA) of two nodes
in a binary tree.

Pattern:
DFS + Recursion

Key Observation:
- If current node is p or q, return it.
- If both subtrees return non-None nodes,
  current node is the LCA.
- Otherwise, propagate the non-None result.

Approaches:
1. Recursive DFS.

Complexity:
Time: O(N)
Space: O(H) recursion stack.
"""

# --------------------------------------------------
# Tree Node
# --------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# Lowest Common Ancestor
# --------------------------------------------------

def lowest_common_ancestor(root, p, q):

    # Base case
    if root is None:
        return None

    # Found one of the target nodes
    if root is p or root is q:
        return root

    # Search left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # Targets found in opposite subtrees
    if left and right:
        return root

    # Propagate the non-None result
    if left:
        return left

    return right


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

    # Target nodes
    p = root.left.left       # Node 4
    q = root.left.right      # Node 5

    lca = lowest_common_ancestor(root, p, q)
    print("LCA of 4 and 5:", lca.val if lca else None)

    p = root.left.left       # Node 4
    q = root.right.left      # Node 6

    lca = lowest_common_ancestor(root, p, q)
    print("LCA of 4 and 6:", lca.val if lca else None)

    p = root.left            # Node 2
    q = root.left.left       # Node 4

    lca = lowest_common_ancestor(root, p, q)
    print("LCA of 2 and 4:", lca.val if lca else None)

    print("Empty Tree:", lowest_common_ancestor(None, p, q))
