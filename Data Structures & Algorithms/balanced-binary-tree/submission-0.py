# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0

        def height(node):
            nonlocal diff
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            diff = max(abs(left-right),diff)

            return max(left,right) + 1    
        height(root)
        return  diff < 2 
        