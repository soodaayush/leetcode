# https://leetcode.com/problems/sum-of-left-leaves

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left
# child of another node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: list[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        left_leaves = []

        def traverse(root, isLeft):
            if not root:
                return

            if not root.left and not root.right and isLeft:
                left_leaves.append(root.val)
                return

            traverse(root.left, True)
            traverse(root.right, False)

        traverse(root, True)

        return sum(left_leaves)

soln = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(soln.sumOfLeftLeaves(root))