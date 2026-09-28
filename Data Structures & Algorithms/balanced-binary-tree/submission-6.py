# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, curr):
        
        if not curr :
            return 0
        leftH = self.height(curr.left)
        rightH = self.height(curr.right)

        return 1 + max(leftH,rightH)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftH = self.height(root.left)
        rightH = self.height(root.right)
        # print(f'the result of {root.val} is {abs(leftH - rightH)}')
        if abs(leftH - rightH) > 1:
            return False
        leftSub = self.isBalanced(root.left)
        rightSub = self.isBalanced(root.right)
        return leftSub and rightSub