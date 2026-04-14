"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}

        curr_new = Node(0)
        curr = head
        

        while curr:
            new = Node(curr.val)
            hash_map[curr] = new
            curr = curr.next
            curr_new.next = new
            curr_new = new

        curr = head
        while curr:
            curr_new = hash_map.get(curr)
            random = hash_map.get(curr.random)
            curr_new.random = random
            curr = curr.next




        return hash_map.get(head,head)   
            