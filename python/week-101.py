# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
# the values in the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next # First term in pair
            second = cur.next.next # Second term in pair
            next_group = second.next # Next group of pairs

            second.next = first # Reverse the pair
            first.next = next_group # Connect first node to rest of nodes
            cur.next = second # Connect previous part

            cur = first # Move forward to next pair

        return dummy.next



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
# e = ListNode(4)
# f = ListNode(4)
# g = ListNode(5)

a.next = b
b.next = c
c.next = d
# d.next = e
# e.next = f
# f.next = g

l1 = a

sol = Solution()

list = sol.swapPairs(l1)

while list:
    print(list.val, end="->")
    list = list.next

