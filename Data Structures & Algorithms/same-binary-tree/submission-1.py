# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def check(p_node,q_node):
            if not p_node and not q_node:
                return None
            elif (p_node and not q_node) or (not p_node and q_node):
                self.same = False  
                return None

            if p_node.val != q_node.val:
                self.same = False                    

            check(p_node.left, q_node.left)
            check(p_node.right, q_node.right)    

        check(p,q)    

        return self.same
        