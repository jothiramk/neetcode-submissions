# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root:Optional[TreeNode]):
            if not root:
                return [True,0]

            isBalanced_left, height_left = dfs(root.left)
            isBalanced_right, height_right = dfs(root.right)
            # A node is balanced if:
            #     Left subtree is balanced
            #     Right subtree is balanced
            #     Height difference ≤ 1

            balanced = (isBalanced_left and isBalanced_right and abs(height_left - height_right ) <= 1)

            return [balanced, 1+max(height_left, height_right)]

        balanced, height = dfs(root)
        return balanced
