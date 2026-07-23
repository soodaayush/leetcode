# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: list[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            targetSum -= root.val

            if targetSum == 0:
                return True
            else:
                return False

        targetSum -= root.val

        return Solution.hasPathSum(self, root.left, targetSum) or Solution.hasPathSum(self, root.right, targetSum)


soln = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(soln.hasPathSum(root, 5))
