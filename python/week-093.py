# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
# linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        unique_values = set()

        prev = head
        next = head

        while next:
            if next.val not in unique_values:
                unique_values.add(next.val)
                prev = next
                next = next.next
            else:
                prev.next = next.next
                next = next.next

        return head






a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

d.next = e
e.next = f

list1 = a
list2 = d

sol = Solution()
merged_list = sol.deleteDuplicates(list1)

while merged_list:
    print(merged_list.val, end="->")
    merged_list = merged_list.next