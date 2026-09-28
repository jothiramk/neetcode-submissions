# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preOrder(self, root, res):
        if not root:
            res.append(root)
            return 
        res.append(root.val)
        self.preOrder(root.left,res)
        self.preOrder(root.right,res)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pPreoreder, qPreoreder = [], []
        self.preOrder(p,pPreoreder)
        self.preOrder(q,qPreoreder)
        print(pPreoreder)
        print(qPreoreder)
        return pPreoreder == qPreoreder