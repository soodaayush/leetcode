# https://leetcode.com/problems/middle-of-the-linked-list/

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        list_for_counting = head
        list_for_locating = head

        i = 0
        j = 0

        while list_for_counting:
            i += 1
            list_for_counting = list_for_counting.next

        while list_for_locating:
            if j == (i // 2):
                return list_for_locating

            list_for_locating = list_for_locating.next
            j += 1






a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

list1 = a

sol = Solution()
merged_list = sol.middleNode(list1)

while merged_list:
    print(merged_list.val, end="->")
    merged_list = merged_list.next
