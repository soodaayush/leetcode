# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If
# the two linked lists have no intersection at all, return null.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        dummyA = headA
        dummyB = headB

        while dummyA != dummyB: # While pointers are not equal to one another
            if dummyA: # Checks if node exists
                dummyA = dummyA.next # Iterates through dummyA
            else:
                dummyA = headB # Otherwise, switch to other list to travel the same distance

            if dummyB: # Checks if node exists
                dummyB = dummyB.next # Iterates through dummyB
            else:
                dummyB = headA # Otherwise, switch to other list to travel the same distance

        return dummyB



a = ListNode(1)
b = ListNode(9)
c = ListNode(1)
d = ListNode(2)
e = ListNode(4)

f = ListNode(3)
g = ListNode(2)
h = ListNode(4)

a.next = b
b.next = c
c.next = d

d.next = e

f.next = d
# g.next = h

l1 = a
l2 = f

sol = Solution()

list = sol.getIntersectionNode(l1, l2)

while list:
    print(list.val, end="->")
    list = list.next

