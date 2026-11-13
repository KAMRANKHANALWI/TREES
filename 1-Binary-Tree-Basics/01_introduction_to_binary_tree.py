
"""
01. Introduction to Binary Tree

Topics:
1. Tree Terminology
2. Types of Binary Trees
3. Binary Tree Representation
4. Constructing a Binary Tree
5. Recursive Call Stack
6. Building Results During Recursion


--------------------------------------------------
1. BINARY TREE
--------------------------------------------------

A Binary Tree is a hierarchical data structure
where each node can have at most two children:

    - Left Child
    - Right Child


Example:

                 1
               /   \
              2     3
             / \   / \
            4   5 6   7


--------------------------------------------------
2. TREE TERMINOLOGY
--------------------------------------------------

Root:
    The topmost node of the tree.

Parent:
    A node that has one or more children.

Child:
    A node directly connected below another node.

Leaf:
    A node with no children.

Sibling:
    Nodes sharing the same parent.

Subtree:
    A node and all its descendants.

Depth:
    Number of edges from root to a node.

Height:
    Number of edges on the longest downward
    path from a node to a leaf.


--------------------------------------------------
3. TYPES OF BINARY TREES
--------------------------------------------------

Full Binary Tree:
    Every node has either 0 or 2 children.

Complete Binary Tree:
    Every level is filled except possibly
    the last, which is filled left to right.

Perfect Binary Tree:
    All internal nodes have 2 children
    and all leaves are at the same level.

Balanced Binary Tree:
    Left and right subtree heights differ
    by at most 1 at every node.

Degenerate Binary Tree:
    Every parent has only one child.


--------------------------------------------------
4. BINARY TREE REPRESENTATION
--------------------------------------------------

Each node stores:

    val   -> Node value
    left  -> Reference to left child
    right -> Reference to right child
"""


# --------------------------------------------------
# 1. TREE NODE CLASS
# --------------------------------------------------

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# --------------------------------------------------
# 2. CONSTRUCTING A BINARY TREE
# --------------------------------------------------

"""
Tree to construct:

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


# --------------------------------------------------
# 3. UNDERSTANDING RECURSION ON TREES
# --------------------------------------------------

"""
Consider this smaller tree:

             1
           /   \
          2     3


We use Preorder as a demonstration.

Preorder:
    Root -> Left -> Right


FUNCTION:

def preorder(root, ans):

    if root is None:
        return

    ans.append(root.val)

    preorder(root.left, ans)
    preorder(root.right, ans)


IMPORTANT:

root.val gets processed BEFORE recursive calls.

For node 1:
    ans.append(1)

Then its left subtree is processed.

For node 2:
    ans.append(2)

Then its children are processed.

After node 2 finishes, execution returns to node 1.

Then node 1's right subtree is processed.

For node 3:
    ans.append(3)


--------------------------------------------------
CALL STACK JOURNEY
--------------------------------------------------

Initial:

    ans = []


STEP 1: preorder(1)

    Stack:

    ┌────────────────────┐
    │ preorder(1)        │ <- TOP
    └────────────────────┘

    root.val = 1

    ans.append(1)

    ans = [1]

    Next: preorder(2)


STEP 2: preorder(2)

    Stack:

    ┌────────────────────┐
    │ preorder(2)        │ <- TOP
    ├────────────────────┤
    │ preorder(1)        │ (PAUSED)
    └────────────────────┘

    root.val = 2

    ans.append(2)

    ans = [1, 2]

    Next: preorder(None)


STEP 3: preorder(None)

    Stack:

    ┌────────────────────┐
    │ preorder(None)     │ <- TOP
    ├────────────────────┤
    │ preorder(2)        │
    ├────────────────────┤
    │ preorder(1)        │
    └────────────────────┘

    Base case is true.

    return

    preorder(None) is POPPED.


STEP 4: preorder(2.right)

    Node 2's right child is also None.

    preorder(None) -> RETURN

    Both children of node 2 are processed.

    preorder(2) -> RETURN

    Stack:

    ┌────────────────────┐
    │ preorder(1)        │ <- TOP
    └────────────────────┘

    Parent resumes.

    ans = [1, 2]


STEP 5: preorder(3)

    Stack:

    ┌────────────────────┐
    │ preorder(3)        │ <- TOP
    ├────────────────────┤
    │ preorder(1)        │ (PAUSED)
    └────────────────────┘

    root.val = 3

    ans.append(3)

    ans = [1, 2, 3]


STEP 6: Process node 3's children.

    preorder(None) -> RETURN
    preorder(None) -> RETURN

    preorder(3) -> RETURN

    preorder(1) -> RETURN


FINAL:

    Stack = EMPTY

    ans = [1, 2, 3]


--------------------------------------------------
IMPORTANT OBSERVATIONS
--------------------------------------------------

1. Every recursive call gets its own stack frame.

2. Parent calls remain paused while child calls execute.

3. Base cases stop further recursive calls.

4. Returning removes the current stack frame.

5. Parent execution resumes from the next statement.

6. In Preorder, the node is processed BEFORE
   calling its left and right children.

7. ans.append(root.val) happens immediately
   when a non-None node is entered.

8. Returning from a function does not remove
   previously appended values from ans.

9. All recursive calls share the SAME ans list
   when it is passed as an argument.


--------------------------------------------------
4. BUILDING THE RESULT LIST
--------------------------------------------------

APPROACH A: SHARED LIST

ans = []

preorder(root, ans)


Each recursive call receives the same list.

    preorder(1, ans)
          |
          | append(1)
          |
    preorder(2, ans)
          |
          | append(2)
          |
    preorder(None, ans)
          |
          | return
          |
    preorder(1) resumes
          |
    preorder(3, ans)
          |
          | append(3)


Result progression:

    []
     |
     v
    [1]
     |
     v
    [1, 2]
     |
     v
    [1, 2]
     |
     v
    [1, 2, 3]


APPROACH B: RETURNING LISTS

def preorder(root):

    if root is None:
        return []

    left = preorder(root.left)
    right = preorder(root.right)

    return [root.val] + left + right


Here, lists are combined while returning.

For node 2:

    left  = []
    right = []

    return [2] + [] + []

    Result = [2]


For node 3:

    left  = []
    right = []

    return [3] + [] + []

    Result = [3]


For node 1:

    left  = [2]
    right = [3]

    return [1] + [2] + [3]

    Result = [1, 2, 3]


Difference:

    Shared List:
        Append while going DOWN.

    Return List:
        Combine results while coming UP.

We will primarily use the shared-list
approach for our initial traversal problems.


--------------------------------------------------
5. PREORDER IMPLEMENTATION
--------------------------------------------------
"""


def preorder(root, ans):

    # Base Case:
    # Empty subtree has nothing to process.
    if root is None:
        return

    # Process current node BEFORE its children.
    ans.append(root.val)

    # Process left subtree.
    preorder(root.left, ans)

    # Process right subtree.
    preorder(root.right, ans)


# --------------------------------------------------
# 6. RETURN-BASED PREORDER IMPLEMENTATION
# --------------------------------------------------


def preorder_return(root):

    # Base Case:
    if root is None:
        return []

    # Get results from both subtrees.
    left = preorder_return(root.left)
    right = preorder_return(root.right)

    # Combine while returning.
    return [root.val] + left + right


# --------------------------------------------------
# 7. EXECUTION
# --------------------------------------------------

if __name__ == "__main__":

    ans = []

    preorder(root, ans)

    print("Preorder using shared list:", ans)

    print(
        "Preorder using return list:",
        preorder_return(root)
    )

    # Output:
    #
    # Preorder using shared list:
    # [1, 2, 4, 5, 3, 6, 7]
    #
    # Preorder using return list:
    # [1, 2, 4, 5, 3, 6, 7]


# --------------------------------------------------
# 8. COMPLEXITY
# --------------------------------------------------

"""
For N nodes and tree height H:

Time Complexity:

    Shared List:
        O(N)

        Every node is visited once.

    Return List:
        O(N^2) worst case with repeated list
        concatenation, due to copying.

Auxiliary Space:

    Recursive Call Stack:
        O(H)

    Shared Result List:
        O(N)

    Balanced Tree:
        H = O(log N)

    Skewed Tree:
        H = O(N)


--------------------------------------------------
TAKEAWAY
--------------------------------------------------

A Binary Tree node contains:

    Value + Left Reference + Right Reference


Tree recursion:

    Go Down
        |
        v
    Reach Base Case
        |
        v
    Return
        |
        v
    Resume Parent
        |
        v
    Continue Processing


Result Building:

    Preorder:
        Process while going DOWN.

    Postorder:
        Process after both children return.

    Inorder:
        Process after left child returns
        and before right child begins.


Understand BOTH:

    1. Recursive Call Stack
    2. Result Construction

These two concepts are fundamental to
solving Binary Tree problems.
"""
