# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        res = 0
        max_val = root.val
        q.append((root,max_val))

        while q:
            for i in range(len(q)):
                curr,max_value = q.popleft()

                if curr.val >= max_value:
                    res+=1            
                
                max_value = max(max_value,curr.val)
                if curr.left:
                    q.append((curr.left,max_value))
                if curr.right:
                    q.append((curr.right,max_value))

        return res