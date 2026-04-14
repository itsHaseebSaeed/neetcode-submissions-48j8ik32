# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = curr = ListNode(0)

        while l1 or l2 or carry:
            first = 0
            second = 0
            if l1:
                first = l1.val
                l1 = l1.next
            if l2:
                second = l2.val 
                l2 = l2.next

            new_val = first + second + carry
            carry = 0

            if new_val >= 10:
                carry = 1
                new_val = new_val - 10

            node = ListNode(new_val)
            curr.next = node
            curr = curr.next    

        return root.next
