# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        #left most at each level
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            temp  = []
            res.append(queue[-1].val)

            for _ in range(len(queue)):
                parent = queue.popleft()
                if parent.left:
                    queue.append(parent.left)
                if parent.right:    
                    queue.append(parent.right)

        return res        



        