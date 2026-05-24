# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋
# denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if head is None: return None

        prev = ListNode(0)
        prev.next = head

        slow = prev
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return prev.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
#
a.next = b
b.next = c
c.next = d
#
# d = ListNode(5)
# e = ListNode(6)
# f = ListNode(4)
#
# d.next = e
# e.next = f

l1 = a
# l2 = d

sol = Solution()

list = sol.deleteMiddle(l1)

while list:
    print(list.val, end="->")
    list = list.next