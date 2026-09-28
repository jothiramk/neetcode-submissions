# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # res = []

        def preorder(root, res):
            if not root:
                res.append(root)
                return 
            
            res.append(root.val)
            preorder(root.left,res)
            preorder(root.right,res)
            
        left , right = [],[]
        preorder(p,left)
        preorder(q,right)
        
        # print(f'{left} {right}')
        return left == right