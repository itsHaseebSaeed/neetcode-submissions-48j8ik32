# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# D[1,2,3,4]
# ^ ^
# D[1,2,3,4]
# ^   ^
# D[1,2,3,4]
#   ^   ^
# D[1,2,3,4]
#     ^   ^
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        first,second = dummy,dummy

        for _ in range(n):
            second = second.next
        while second.next:
            first = first.next
            second = second.next
            
        dest = first.next.next

        first.next = dest

        return dummy.next
                

        