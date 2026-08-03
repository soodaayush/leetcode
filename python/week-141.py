# https://leetcode.com/problems/subtree-of-another-tree/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
# with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree, tree, is a tree that consists of a node in tree and all of this node's
# descendants. The tree, tree, could also be considered as a subtree of itself.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: list[TreeNode], subRoot: list[TreeNode]) -> bool:
        if (not root.left and not root.right) and (not subRoot.left and not subRoot.right) and (
                root.val != subRoot.val):
            return False

        root_vals = []
        subroot_vals = []

        def traverse(root, arr):
            if not root:
                arr.append(None)
                return

            arr.append(root.val)
            traverse(root.left, arr)
            traverse(root.right, arr)

        traverse(root, root_vals)
        traverse(subRoot, subroot_vals)

        root_str = ",".join([str(num) for num in root_vals])
        subroot_str = ",".join([str(num) for num in subroot_vals])

        return subroot_str in root_str


soln = Solution()

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(soln.isSubtree(root, subRoot))
