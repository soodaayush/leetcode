# https://leetcode.com/problems/remove-linked-list-elements/

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
# and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        ans = ListNode(0, head) # Initialize linked list with a safe node of 0 at the beginning
        dummy = ans # Create dummy pointer for ans

        while dummy:
            while dummy.next and dummy.next.val == val: # If next value is = val, then skip over it
                dummy.next = dummy.next.next
            dummy = dummy.next # Iterate over linked list one position at a time

        return ans.next # Return filtered list

a = ListNode(7)
b = ListNode(7)
c = ListNode(7)
d = ListNode(7)
# e = ListNode(4)
# f = ListNode(5)
# g = ListNode(6)

a.next = b
b.next = c
c.next = d
# d.next = e
# e.next = f
# f.next = g

l1 = a

sol = Solution()

list = sol.removeElements(l1, 7)

while list:
    print(list.val, end="->")
    list = list.next

