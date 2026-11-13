
"""
02. Inorder Traversal

Problem:
Given the root of a Binary Tree, return its
Inorder Traversal.

Pattern:
DFS + Recursion

Key Observation:
Inorder = Left -> Root -> Right

The current node is processed only after
its entire left subtree has been completed.


--------------------------------------------------
VISUAL INTUITION
--------------------------------------------------

                 1
               /   \
              2     3
             / \   / \
            4   5 6   7

Inorder:

4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7


--------------------------------------------------
RECURSIVE CALL STACK
--------------------------------------------------

Consider:

             1
           /   \
          2     3
         / \
        4   5

Execution:

inorder(1)
    |
    └── inorder(2)
            |
            └── inorder(4)
                    |
                    └── inorder(None)
                            |
                            ↓
                          RETURN

inorder(4) resumes:
    ans.append(4)
    ans = [4]

    inorder(4.right) -> RETURN

inorder(4) -> RETURN

inorder(2) resumes:
    ans.append(2)
    ans = [4, 2]

    inorder(5)
        |
        ├── inorder(None) -> RETURN
        |
        ├── ans.append(5)
        |       ans = [4, 2, 5]
        |
        └── inorder(None) -> RETURN

inorder(2) -> RETURN

inorder(1) resumes:
    ans.append(1)
    ans = [4, 2, 5, 1]

    inorder(3)
        |
        ├── inorder(None) -> RETURN
        |
        ├── ans.append(3)
        |       ans = [4, 2, 5, 1, 3]
        |
        └── inorder(None) -> RETURN

FINAL:
    [4, 2, 5, 1, 3]


--------------------------------------------------
APPROACH 1: RECURSIVE
--------------------------------------------------

Pseudocode:

inorder(root):

    if root is None:
        return

    inorder(root.left)

    process(root)

    inorder(root.right)


--------------------------------------------------
CODE
--------------------------------------------------
"""

# --------------------------------------------------
# TREE NODE CLASS
# --------------------------------------------------

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_recursive(root, ans):

    # Base Case:
    # Empty subtree -> nothing to process.
    if root is None:
        return

    # 1. Process the entire left subtree.
    inorder_recursive(root.left, ans)

    # 2. Process the current node.
    ans.append(root.val)

    # 3. Process the entire right subtree.
    inorder_recursive(root.right, ans)

    return ans


# --------------------------------------------------
# APPROACH 2: ITERATIVE USING STACK
# --------------------------------------------------

"""
Idea:

Recursion internally uses a call stack.

Here, we explicitly create and manage a stack.

1. Keep moving left and push nodes.
2. When left becomes None, pop a node.
3. Process the popped node.
4. Move to its right child.
5. Repeat until both current and stack are empty.
"""


def inorder_iterative(root):

    stack = []
    ans = []

    current = root

    while current or stack:

        # Keep going left.
        while current:

            stack.append(current)

            current = current.left

        # Process the most recently stored node.
        current = stack.pop()

        ans.append(current.val)

        # Explore its right subtree.
        current = current.right

    return ans


# --------------------------------------------------
# EXAMPLE
# --------------------------------------------------

if __name__ == "__main__":

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    ans = []

    print("Recursive:", inorder_recursive(root, ans))

    print("Iterative:", inorder_iterative(root))

    # Output:
    #
    # Recursive: [4, 2, 5, 1, 6, 3, 7]
    # Iterative: [4, 2, 5, 1, 6, 3, 7]


# --------------------------------------------------
# COMPLEXITY
# --------------------------------------------------

"""
Let N = Number of nodes.
Let H = Height of the tree.

RECURSIVE:

Time  -> O(N)
Space -> O(H) auxiliary recursion stack.

ITERATIVE:

Time  -> O(N)
Space -> O(H) auxiliary explicit stack.

Balanced Tree:
    H = O(log N)

Skewed Tree:
    H = O(N)


--------------------------------------------------
TAKEAWAY
--------------------------------------------------

Inorder = LEFT -> ROOT -> RIGHT

The current node is processed after
the left recursive call returns.

Remember:

Preorder:
    Process while going DOWN.

Inorder:
    Process between left and right.

Postorder:
    Process after both children return.
"""
