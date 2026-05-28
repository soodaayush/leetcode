# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
# from the original list. Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        seen = {}
        ans = ListNode(0, head)

        dummy = head
        unique = ans

        while dummy:
            if dummy.val not in seen:
                seen[dummy.val] = 1
            else:
                seen[dummy.val] += 1

            dummy = dummy.next

        while unique:
            if unique.next and seen[unique.next.val] > 1:
                unique.next = unique.next.next
            else:
                unique = unique.next

        return ans.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

l1 = a

sol = Solution()

list = sol.deleteDuplicates(l1)

while list:
    print(list.val, end="->")
    list = list.next

