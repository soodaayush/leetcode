# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
# leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: list[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left) # Find max depth of left nodes
        right = self.maxDepth(root.right) # Find max depth of right nodes

        return max(left, right) + 1 # Add one for each node that is deeper in the tree


root = TreeNode(3)

root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

soln = Solution()
print(soln.maxDepth(root))