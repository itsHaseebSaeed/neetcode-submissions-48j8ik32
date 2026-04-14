# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [] # [[1],]
        queue = deque() #[2 3]
        queue.append(root)

        while queue:
            temp = [] # [1]
            for node in queue:
                temp.append(node.val)
            res.append(temp)
            for _ in range(len(queue)):
                parent = queue.popleft()
                if parent.left:
                    queue.append(parent.left)
                if parent.right:    
                    queue.append(parent.right)    
        return res        