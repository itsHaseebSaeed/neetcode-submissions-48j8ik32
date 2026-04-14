# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node,lastGoodNode):
            nonlocal count
            if not node:
                return None

            if node.val >= lastGoodNode:
                count += 1  
                lastGoodNode = node.val  

            dfs(node.left,lastGoodNode)
            dfs(node.right,lastGoodNode)

        dfs(root,root.val)    
        return count

        