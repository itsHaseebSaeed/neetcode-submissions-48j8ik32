# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node,depth):
            nonlocal res

            if not node:
                return 0
            
            left = dfs(node.left, depth+1) # 0
            right = dfs(node.right, depth+1) # 

            res = max(res, right+left)

            return max(right, left) + 1

        dfs(root,1)    
        return res




        