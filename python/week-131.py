# https://leetcode.com/problems/binary-tree-paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: list[TreeNode]) -> list[str]:
        arr_paths = []
        temp = []

        def traverse(root):
            if root is None:
                return
            temp.append(str(root.val))
            if not root.left and not root.right:
                arr_paths.append("->".join(temp))
            else:
                traverse(root.right)
                traverse(root.left)

            temp.pop()

        traverse(root)

        return arr_paths


soln = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

print(soln.binaryTreePaths(root))
