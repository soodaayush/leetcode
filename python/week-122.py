# https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: list[TreeNode], q: list[TreeNode]) -> bool:
        arr1 = [] # Arrays for traversing trees
        arr2 = []

        def traversal(root, arr):
            if root is None:
                arr.append(None) # Append null when there is no node present
                return

            arr.append(root.val) # Preorder traversal - visits node, then goes as far left as possible, the goes to right node
            traversal(root.left, arr)
            traversal(root.right, arr)

        traversal(p, arr1) # Run function for both trees
        traversal(q, arr2)

        return arr1 == arr2 # Check if arrays are the same


soln = Solution()

root1 = TreeNode(1)

root1.left = TreeNode(2)
root1.right = TreeNode(1)


root2 = TreeNode(1)

root2.left = TreeNode(1)
root2.right = TreeNode(2)

print(soln.isSameTree(root1, root2))