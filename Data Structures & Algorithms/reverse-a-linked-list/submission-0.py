# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# none <- 0 -> 1 -> 2 -> 3

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr :
            nxt = curr.next # save next
            curr.next = prev # change next
            prev = curr
            curr = nxt
        return prev
        