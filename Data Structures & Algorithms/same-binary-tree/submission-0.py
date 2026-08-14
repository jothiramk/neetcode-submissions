# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # res = []

        def preorder(root):
            if not root:
                res.append(root)
                return 
            
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
        res = []
        preorder(p)
        left = res
        res = []
        preorder(q)
        right = res
        print(f'{left} {right}')
        return left == right