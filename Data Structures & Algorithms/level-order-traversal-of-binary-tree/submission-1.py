# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        Q = []
        Q.append((root,1))
        level = []
        currLevel = 1


        while Q:
            node,depth = Q.pop(0)
            if not node:
                continue

            if depth > currLevel:
                currLevel = depth
                res.append(level)
                level = []

            level.append(node.val)
            Q.append((node.left,depth+1))
            Q.append((node.right,depth+1))

        res.append(level)
        return res



        