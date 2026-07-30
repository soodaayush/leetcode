# https://leetcode.com/problems/binary-tree-level-order-traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from
# left to right, level by level).

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: list[TreeNode]) -> list[list[int]]:
        levels = []

        if not root:
            return levels

        q = deque()
        q.append(root)

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            levels.append(level)

        return levels


soln = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(soln.levelOrder(root))
