# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = head
        prev = head
        current = head

        counter = 1
        length = 0

        while dummy:
            length += 1
            dummy = dummy.next

        position = length - (n - 1)

        if position == 1:
            return prev.next

        while head:
            if counter == position:
                prev.next = current.next
                return head
            else:
                prev = current
                current = current.next

            counter += 1



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)


d = ListNode(4)
e = ListNode(5)

a.next = b
# b.next  = c
# c.next = d
# d.next = e

l1 = a


sol = Solution()

list = sol.removeNthFromEnd(l1, 2)

while list:
    print(list.val, end="->")
    list = list.next