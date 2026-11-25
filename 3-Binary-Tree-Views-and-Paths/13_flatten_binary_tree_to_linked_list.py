
"""
Problem:
Flatten a Binary Tree into a Linked List in-place.

The linked list must follow Preorder Traversal:
Root -> Left -> Right

Requirements:
- Every left pointer must become None.
- Every right pointer must point to the next node in preorder.
- Rearrange existing nodes; do not create new nodes.

Pattern:
In-place Tree Modification + Preorder

Key Observation:
Move the left subtree to the right.
Attach the original right subtree to the rightmost
node of the moved left subtree.

Approach:
1. Save the original right subtree.
2. Move the left subtree to the right.
3. Set the left pointer to None.
4. Find the rightmost node of the moved subtree.
5. Attach the saved right subtree there.
6. Move to the next node.

Complexity:
Time: O(N^2) worst case
Space: O(1)
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flatten(root):
    curr = root

    while curr:

        if curr.left:

            # Save the original right subtree
            right_subtree = curr.right

            # Move left subtree to the right
            curr.right = curr.left
            curr.left = None

            # Find the rightmost node of the moved subtree
            temp = curr.right

            while temp.right:
                temp = temp.right

            # Attach the original right subtree
            temp.right = right_subtree

        # Move to the next node
        curr = curr.right


# Print the flattened tree using right pointers
def print_flattened(root):
    curr = root

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.right

    print("None")


if __name__ == "__main__":

    # Test Case 1: Standard tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    flatten(root)

    print("Flattened Tree:")
    print_flattened(root)

    # Expected:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

    # Test Case 2: Single node
    single = TreeNode(10)
    flatten(single)

    print("\nSingle Node:")
    print_flattened(single)

    # Expected:
    # 10 -> None

    # Test Case 3: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)

    flatten(left_skewed)

    print("\nLeft Skewed:")
    print_flattened(left_skewed)

    # Expected:
    # 1 -> 2 -> 3 -> None

    # Test Case 4: Right-skewed tree
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)

    flatten(right_skewed)

    print("\nRight Skewed:")
    print_flattened(right_skewed)

    # Expected:
    # 1 -> 2 -> 3 -> None

    # Test Case 5: Empty tree
    flatten(None)

    print("\nEmpty Tree:")
    print_flattened(None)

    # Expected:
    # None
