# https://leetcode.com/problems/increasing-order-search-tree/

# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree
# is now the root of the tree, and every node has no left child and only one right child.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: list[TreeNode]) -> list[TreeNode]:
        nodes = []

        def traverse(root):
            if not root:
                return

            nodes.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)

        nodes.sort()
        new_tree = TreeNode(nodes[0])
        tmp = new_tree

        for i in nodes[1:]:
            tmp.left = None
            tmp.right = TreeNode(i)
            tmp = tmp.right

        return new_tree


soln = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

root.right.right = TreeNode(8)

root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

print(soln.increasingBST(root))
