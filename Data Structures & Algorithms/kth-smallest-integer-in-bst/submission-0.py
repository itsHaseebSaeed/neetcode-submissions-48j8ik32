# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = -1
        index = 0
        def dfs(node):
            nonlocal kth,index

            if not node:
                return None

            dfs(node.left)

            index += 1

            if index == k:
                kth = node.val
                return None
        
            dfs(node.right)

        dfs(root)
        return kth
        