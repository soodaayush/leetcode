# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        node = None # Set previous node to none initially

        while head:
            temp = head.next # Store a temporary variable containing the next nodes in the linked list so connection is not lost
            head.next = node # Set the pointer of the current node to the previous node, reversing the order
            node = head # Set the previous node to the current node for the next iteration
            head = temp # Set the current node to the next node

        return node # Return the reversed list

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

head = a
unreversed_head = head

while unreversed_head:
    print(unreversed_head.val, end="->")
    unreversed_head = unreversed_head.next

print()

sol = Solution()
reversed_head = sol.reverseList(head)

curr = reversed_head

while curr:
    print(curr.val, end="->")
    curr = curr.next
