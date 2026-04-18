# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def search(node):
            if not node:
                # add the node
                return 
            
            if node.val > val:
                if node.left:
                    search(node.left)
                else:
                    node.left = TreeNode(val)   
                    return
            else:
                if node.right:
                    search(node.right)
                else:
                    node.right = TreeNode(val)    
                    return
        search(root)                
        return root
        