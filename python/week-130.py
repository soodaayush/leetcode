# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node
# down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: list[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            if left == 0 or right == 0:
                return max(left, right) + 1
            else:
                return min(left, right) + 1

        return traverse(root)

soln = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(soln.minDepth(root))