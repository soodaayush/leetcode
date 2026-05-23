# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        first_num = []
        second_num = []

        list1 = l1
        list2 = l2

        while list1:
            first_num.append(list1.val)
            list1 = list1.next

        while list2:
            second_num.append(list2.val)
            list2 = list2.next

        first_num.reverse()
        second_num.reverse()

        sum = int("".join(map(str, first_num))) + int("".join(map(str, second_num)))

        result = [int(x) for x in str(sum)]
        result.reverse()

        new_list = ListNode(result[0])
        dummy = new_list

        for i in result[1:]:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return new_list

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next  = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)

d.next = e
e.next = f

l1 = a
l2 = d

sol = Solution()

list = sol.addTwoNumbers(l1, l2)

while list:
    print(list.val, end="->")
    list = list.next