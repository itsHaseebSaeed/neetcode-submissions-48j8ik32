# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        level = []
        currLevel = 1
        Q = deque()
        Q.append([root,1])

        while Q:
            node,depth = Q.popleft()
            if not node:
                continue

            if depth > currLevel:
                currLevel = depth
                res.append(level[-1])
                level=[]

            level.append(node.val)
            Q.append((node.left,depth+1))
            Q.append((node.right,depth+1))

        res.append(level[-1])
        return res    
