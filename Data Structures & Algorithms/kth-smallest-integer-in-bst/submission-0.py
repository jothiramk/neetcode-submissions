# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preOrder(self,root: Optional[TreeNode], res : List):
        if not root:
            return 
        
        self.preOrder(root.left,res)
        res.append(root.val)
        self.preOrder(root.right,res)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorder_list= []
        self.preOrder(root,preorder_list)
        print(preorder_list)
        return preorder_list[k-1]