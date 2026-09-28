# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root, res):
        if not root:
            res.append(root)
            return 
        res.append(root.val)
        self.inOrder(root.left,res)
        self.inOrder(root.right,res)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pInoreder, qInoreder = [], []
        self.inOrder(p,pInoreder)
        self.inOrder(q,qInoreder)
        print(pInoreder)
        print(qInoreder)
        return pInoreder == qInoreder