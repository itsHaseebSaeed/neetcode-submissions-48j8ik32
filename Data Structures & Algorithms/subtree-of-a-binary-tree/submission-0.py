# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        hashes = set()

        def hash(node,store):
            nonlocal hashes
            if not node:
                return "N"

            left = hash(node.left,store) 
            right = hash(node.right,store)

            hash_str = f"({node.val}#{left}#{right})"
            if store:
                hashes.add(hash_str)
            return hash_str

        hash(root,store=True)
        sub = hash(subRoot,store=False)

        return sub in hashes