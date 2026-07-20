# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Given the root of a binary tree, return the postorder traversal of its
# nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: list[TreeNode]) -> list[int]:
        arr = []

        def traversal(root):
            if not root:
                return

            traversal(root.left)
            traversal(root.right)
            arr.append(root.val)

        traversal(root)

        return arr

soln = Solution()

root = TreeNode(1)

root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(soln.postorderTraversal(root))