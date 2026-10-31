# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Check if array is sorted in ascending order
        for i in range(1,len(res)):
            if res[i-1] >= res[i]:  # Strictly increasing, so >= means invalid
                return False
        return True
            