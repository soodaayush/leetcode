# https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: list[TreeNode]) -> bool:
        arr_left = []
        arr_right = []

        def traverse_left(root):
            if root is None:
                arr_left.append(None)
                return

            arr_left.append(root.val)
            traverse_left(root.left)
            traverse_left(root.right)

        def traverse_right(root):
            if root is None:
                arr_right.append(None)
                return

            arr_right.append(root.val)
            traverse_right(root.right)
            traverse_right(root.left)

        traverse_left(root.left)
        traverse_right(root.right)

        return arr_left == arr_right

soln = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(3)

root.right.right = TreeNode(3)

print(soln.isSymmetric(root))
