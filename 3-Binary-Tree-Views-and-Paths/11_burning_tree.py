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


def burning_tree(root, target):
    if root is None or target is None:
        return 0

    parent = build_parent_map(root)

    queue = deque([target])
    visited = {target}

    time = 0

    while queue:
        level_size = len(queue)
        burned_something = False

        for _ in range(level_size):
            node = queue.popleft()

            # Left child
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)
                burned_something = True

            # Right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)
                burned_something = True

            # Parent
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                queue.append(parent[node])
                burned_something = True

        if burned_something:
            time += 1

    return time


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    target = root.left.right

    print("Burning Time:", burning_tree(root, target))
