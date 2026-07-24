# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: list[TreeNode]) -> bool:
        def traverse(root):
            if root is None:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            if left == -1:
                return -1
            elif right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1

        balanced = traverse(root)

        return balanced > -1


soln = Solution()

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(soln.isBalanced(root))
