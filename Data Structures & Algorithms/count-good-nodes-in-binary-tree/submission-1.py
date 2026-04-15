# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node,prevHigh):
            nonlocal count
            if not node:
                return 


            if node.val >= prevHigh:
                count+=1
                prevHigh = node.val

            dfs(node.left,prevHigh)
            dfs(node.right,prevHigh)    
        dfs(root,root.val)
        return count