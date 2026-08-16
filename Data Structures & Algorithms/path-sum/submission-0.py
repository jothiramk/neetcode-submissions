# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def dfs(root : Optional[TreeNode],targetSum, sum_path):
            if not root:
                return False

            sum_path += root.val            
            if not root.left and not root.right and sum_path == targetSum:
                return True
            
            
            if dfs(root.left, targetSum, sum_path):
                return True
            if dfs(root.right, targetSum, sum_path):
                return True
            return False
        
        res = 0
        return dfs(root,targetSum, res)
        


        
        