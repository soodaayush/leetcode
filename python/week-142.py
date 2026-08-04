# https://leetcode.com/problems/search-in-a-binary-search-tree/

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree
# rooted with that node. If such a node does not exist, return null.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: list[TreeNode], val: int) -> list[TreeNode]:
        sub_root = None

        def traverse(root):
            nonlocal sub_root

            if not root:
                return

            if root.val == val:
                sub_root = root
                return

            traverse(root.left)
            traverse(root.right)

        traverse(root)

        return sub_root



soln = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val = 2

print(soln.searchBST(root, val))
