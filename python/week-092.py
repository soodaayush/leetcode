# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        new_list = ListNode()
        dummy = new_list # Used as a placeholder node to make inserting easier

        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2 # Appends list2 value into new list
                list2 = list2.next # list2 is iterated
            else:
                dummy.next = list1 # Appends list1 value into new list
                list1 = list1.next # list1 is iterated

            dummy = dummy.next # Appends head of merged linked list

        if list1: # If list 1 is not empty and list2 is empty
            dummy.next = list1
        else: # Vice versa
            dummy.next = list2

        return new_list.next # Print elements of merged list





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
merged_list = sol.mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val, end="->")
    merged_list = merged_list.next