# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def recursion(node):
            if not node:
                return 0

            leftNode = recursion(node.left) 
            rightNode = recursion(node.right) 

            # don't need both node just the longest one
            self.res = max(self.res, leftNode + rightNode)
            return max(leftNode , rightNode) + 1
        recursion(root)    
            
        return self.res   
        