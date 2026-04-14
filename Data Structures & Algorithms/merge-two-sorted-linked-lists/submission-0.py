# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(float("infinity"),None)
        curr = dummy
        
        while list1 and list2:
            val = float("infinity")
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            newNode = ListNode(val,None)
            curr.next = newNode
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2            

        return dummy.next    