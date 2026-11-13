
"""
============================================================
04. POSTORDER TRAVERSAL
============================================================

Problem:
Given the root of a binary tree, return the postorder
traversal of its nodes.

Pattern:
DFS (Depth First Search)

Traversal:
Left -> Right -> Root

Key Observation:
Process the current node only after both its left and
right subtrees have been completely traversed.

Approaches:
1. Recursive DFS
2. Iterative DFS using Two Stacks

Time Complexity:
O(N) - Every node is visited exactly once.

Space Complexity:
Recursive: O(H) auxiliary recursion stack.
Iterative: O(N) auxiliary space for two stacks.
Output: O(N).

============================================================
"""

# ----------------------------------------------------------
# 1. TREE NODE
# ----------------------------------------------------------

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ----------------------------------------------------------
# 2. RECURSIVE APPROACH
# ----------------------------------------------------------

def postorder_recursive(root, ans):
    if root is None:
        return

    # Step 1: Traverse left subtree
    postorder_recursive(root.left, ans)

    # Step 2: Traverse right subtree
    postorder_recursive(root.right, ans)

    # Step 3: Process current node LAST
    ans.append(root.val)

    return ans


# ----------------------------------------------------------
# 3. ITERATIVE APPROACH - TWO STACKS
# ----------------------------------------------------------

def postorder_iterative(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()

        # Store current node in second stack
        stack2.append(node)

        # Push left child
        if node.left:
            stack1.append(node.left)

        # Push right child
        if node.right:
            stack1.append(node.right)

    ans = []

    # Reverse the traversal order
    while stack2:
        ans.append(stack2.pop().val)

    return ans


# ----------------------------------------------------------
# 4. BUILD BINARY TREE
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
# 5. DRIVER CODE
# ----------------------------------------------------------

if __name__ == "__main__":
    root = build_tree()

    recursive_result = postorder_recursive(root, [])
    iterative_result = postorder_iterative(root)

    print("Recursive:", recursive_result)
    print("Iterative:", iterative_result)
