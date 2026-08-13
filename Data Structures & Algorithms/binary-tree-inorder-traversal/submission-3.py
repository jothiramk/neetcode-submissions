# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

# While the current node is not null or the stack is not empty:
    # While the current node is not null, push it onto the stack and move to its left child.
    # Pop a node from the stack, add its value to the result.
    # Move to the right child of the popped node.
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node_visited = stack.pop()
            res.append(node_visited.val)
            curr = node_visited.right
        
        return res
            

