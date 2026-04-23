# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def maxDiameter(node):
            nonlocal res
            if not node:
                return 0

            left = maxDiameter(node.left)
            right = maxDiameter(node.right)

            res = max(res, left + right)
            return max(left,right) + 1

        maxDiameter(root)    
        return res    
