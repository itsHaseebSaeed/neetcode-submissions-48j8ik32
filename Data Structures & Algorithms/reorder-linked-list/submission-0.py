# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        node = head
        def rec(curr):
            if not curr: 
                return node

            h = rec(curr.next)
            if not h:
                return None

            if h == curr or h.next == curr:
                curr.next = None
                return None
            nxt = h.next
            h.next = curr
            curr.next = nxt
            return nxt

        rec(node)    
        

        