# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes
# with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        if not root:
            return good_nodes

        max_seen = root.val

        def traverse(root, max_seen):
            nonlocal good_nodes

            if not root:
                return

            if max_seen <= root.val:
                good_nodes = good_nodes + 1
                max_seen = root.val

            traverse(root.left, max_seen)
            traverse(root.right, max_seen)

        traverse(root, max_seen)

        return good_nodes


soln = Solution()

root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(4)

print(soln.goodNodes(root))
