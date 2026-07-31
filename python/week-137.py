# https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
#     The left subtree of a node contains only nodes with keys strictly less than
#     the node's key.
#     The right subtree of a node contains only nodes with keys strictly greater
#     than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: list[TreeNode]) -> bool:
        def valid(node, min, max):
            if not node:
                return True

            if not (node.val > min and node.val < max):
                return False

            return valid(node.left, min, node.val) and valid(node.right, node.val, max)

        return valid(root, float("-inf"), float("inf"))

soln = Solution()

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(soln.isValidBST(root))