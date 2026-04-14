# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val = self.sumNum(l1,l2)
            if val + carry > 9 :
                val = (val + carry) % 10
                carry = 1
            else:
                val =  val + carry
                carry = 0   

            if l1:      
                l1 = l1.next
            if l2:    
                l2 = l2.next  

            curr.next =  ListNode(val,None)   
            curr = curr.next
        return dummy.next    
            
    def sumNum(self,l1,l2):
        total = 0
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        return v1 + v2



        