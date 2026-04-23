# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        qp = []
        qq = []
        qp.append(p)
        qq.append(q)

        while len(qp) or len(qq):
            nodep = qp.pop(0)
            nodeq = qq.pop(0)

            if not nodep and not nodeq:
                continue
                return True
            elif (nodep and not nodeq) or (nodeq and not nodep):
                return False 

            if nodep.val != nodeq.val:
                return False
            
            qp.append(nodep.left)
            qq.append(nodeq.left)
            qp.append(nodep.right)        
            qq.append(nodeq.right)
        




        return True    

        