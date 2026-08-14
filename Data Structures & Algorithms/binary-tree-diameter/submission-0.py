# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            #diameter at the node
            diameter = left+right
            #keep updating the max diameter at every node
            self.res = max(self.res, diameter)
            #return the max depth at the node to the caller for next computations
            return 1 + max(left,right)
        
        dfs(root)
        return self.res