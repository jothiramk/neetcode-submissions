# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        counter = 1
        q = deque()
        q.append((root,root.val))
        while q:
            curr,max_value = q.popleft()
            if curr.left:
                if curr.left.val >= max_value:
                    counter+=1
                q.append((curr.left,max(curr.left.val,max_value)))
            
            if curr.right:
                if curr.right.val >= max_value:
                    counter+=1
                q.append((curr.right,max(curr.right.val,max_value)))
        return counter