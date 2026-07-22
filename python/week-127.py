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
        def dfs(left, right):
            if not left and not right: # If both nodes are null, must be symmetrical
                return True

            if not left or not right: # If only one node is null, not symmetrical
                return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
            # Above checks if left node == right node, and if their subtreees are equal

        return dfs(root.left, root.right)

soln = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(3)

root.right.right = TreeNode(3)

print(soln.isSymmetric(root))
