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
# For node deletion with two children, we consistently replace the target node with its inorder successor (smallest node in the right subtree). For example, deleting 5 from [5,3,9,1,4] yields [9,3,null,1,4]. Using the inorder predecessor (largest node in the left subtree) would yield [4,3,9,1], which is also a valid BST result.
                minnode = self.min_node(root.right)
                root.val = minnode.val
                root.right = self.deleteNode(root.right,minnode.val)
        return root