# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left_diameter = dfs(root.left)
            right_diameter = dfs(root.right)
            total = left_diameter + right_diameter
            self.res = max(total,self.res)

            return 1 + max(left_diameter, right_diameter)

        dfs(root)
        return self.res