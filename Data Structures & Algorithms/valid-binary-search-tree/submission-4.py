# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #doing inorder dfs should make sure all the values are in order for the BST
        isValid = True
        prev = -math.inf

        def dfs(node):
            nonlocal prev
            nonlocal isValid

            if not node:
                return None

            dfs(node.left)

            if node.val <= prev:
                isValid = False
                return None
            
            prev = node.val

            dfs(node.right)

        dfs(root)
        return isValid        
        