class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    # Definition for a binary tree node.
    left_max = 0
    right_max = 0

    if root is None:
        return 0

    left = maxDepth(root.left)
    print("left", left)
    right = maxDepth(root.right)
    print("right", right)

    return max(left, right) + 1


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

d1 = maxDepth(root=tree)
print(d1)
