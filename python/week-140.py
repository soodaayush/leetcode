# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
# of all the values of the nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: list[TreeNode], k: int) -> int:
        counter = 0
        answer = 0

        def traverse(root):
            nonlocal counter
            nonlocal answer

            if not root:
                return

            traverse(root.left)
            counter += 1

            if counter == k:
                answer = root.val

            traverse(root.right)

        traverse(root)

        return answer


soln = Solution()

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.right = TreeNode(2)

print(soln.kthSmallest(root, 1))
