# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> list[TreeNode]:
        if not preorder and not inorder:
            return None

        root_val = preorder[0]
        root_inorder_index = inorder.index(root_val)

        root = TreeNode(preorder[0])

        left_inorder = inorder[0:root_inorder_index]
        right_inorder = inorder[(root_inorder_index + 1):]

        left_subtree_length = len(left_inorder)

        left_preorder = preorder[1:(left_subtree_length + 1)]
        right_preorder = preorder[(left_subtree_length + 1):]

        root.left = Solution.buildTree(self, left_preorder, left_inorder)
        root.right = Solution.buildTree(self, right_preorder, right_inorder)

        return root

soln = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(soln.buildTree(preorder, inorder))
