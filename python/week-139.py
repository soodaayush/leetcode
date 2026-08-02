# https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of
# the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: list[TreeNode]) -> list[int]:
        vals = []

        if not root:
            return vals

        vals.append(root.val)

        def dfs(root, depth):
            if root is None:
                return

            if depth > len(vals) - 1:
                vals.append(root.val)

            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)

        return vals


soln = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left = TreeNode(4)

print(soln.rightSideView(root))
