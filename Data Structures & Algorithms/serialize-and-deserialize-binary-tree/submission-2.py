# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Codec:
    # 1#2#3#N#N#4#5#N#N#N#N

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        Q = deque()
        Q.append(root)
        res = []
        while Q:
            node = Q.popleft()

            if not node:
                res.append("N")
                continue
            res.append(str(node.val))
                 
            Q.append(node.left)
            
            Q.append(node.right)   
        
        return "#".join(res)


    # 4#5#N#N#N#N
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if len(data) == 0:
            return None
        strArray = data.split("#")
        Q = deque()

        root = TreeNode(int(strArray[0]))   
        Q.append(root)
        i = 1

        while Q:
            curr = Q.popleft()

            if i < len(strArray) and strArray[i] != "N":
                left = TreeNode(strArray[i])
                curr.left = left
                Q.append(left)
            i+=1

            if i < len(strArray) and strArray[i] != "N":
                right = TreeNode(strArray[i])
                curr.right = right
                Q.append(right)
            i+=1

            
        return root    

        





























