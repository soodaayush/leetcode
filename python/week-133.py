# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently
# occurred element) in it.

# If the tree has more than one mode, return them in any order.

# If the tree has more than one mode, return them in any order.
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: list[TreeNode]) -> list[int]:
        frequencies = {}
        most_frequently_occured_elements = []

        def traversal(root):
            if root is None:
                return

            frequencies[root.val] = frequencies.get(root.val, 0) + 1
            traversal(root.left)
            traversal(root.right)

        traversal(root)

        max_freq = max(frequencies.values())

        for i in frequencies:
            if frequencies[i] == max_freq:
                most_frequently_occured_elements.append(i)

        return most_frequently_occured_elements


soln = Solution()

root = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.left = TreeNode(1)

print(soln.findMode(root))
