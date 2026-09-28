# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root : Optional[TreeNode], result : list):
        if not root:
            return
        self.inOrder(root.left,result)
        result.append(root.val)
        self.inOrder(root.right,result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        self.inOrder(root,inorder_list)

        return inorder_list[k-1]