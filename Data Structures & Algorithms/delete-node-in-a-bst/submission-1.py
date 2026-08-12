# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def min_node (self, root : Optional[TreeNode]) -> int:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        # We found the element to delete, 
        else:
            #if it is a leaf node just return opp pointer
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
            #it is not a leaf node, replace the node with any leaf node preferrably the smallest. 
                minnode = self.min_node(root.right)
                root.val = minnode.val
                root.right = self.deleteNode(root.right,minnode.val)
        return root