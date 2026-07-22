# https://leetcode.com/problems/invert-binary-tree/

# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: list[TreeNode]) -> list[TreeNode]:
        inverted_tree = []

        def invert(root):
            if root is None:
                return

            root.left = root.right
            inverted_tree.append(root.left)
            invert(root.left)
            invert(root.right)

        invert(root)

        return inverted_tree


soln = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
