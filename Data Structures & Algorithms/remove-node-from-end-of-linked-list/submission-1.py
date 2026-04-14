# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # [1,2,3,4] n = 2
        #          ^f
        #      ^s
        #save prev
        # prev.next = slow.next
        slow,fast = head,head
        dummy = prev = ListNode(0)
        dummy.next = slow
        prev.next = slow
        for _ in range(n):
            fast = fast.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return dummy.next

