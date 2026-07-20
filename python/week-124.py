# https://leetcode.com/problems/binary-tree-preorder-traversal

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: list[TreeNode]) -> list[int]:
        arr = []

        def traverse(root):
            if root is None:
                return

            arr.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)

        return arr

soln = Solution()

root = TreeNode(1)

root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(soln.preorderTraversal(root))
