"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = None
        curr = head
        #here i am creating all the nodes
        # oldToNew = defaultdict(Node)
        oldToNew ={None: None}

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        # oldToNew[None]: None

        
        for oldNode, newNode in oldToNew.items():
            if oldNode == None:
                continue
            newNode.next = oldToNew[oldNode.next]
            if not newHead:
                newHead = newNode                
            
            newNode.random = oldToNew[oldNode.random]                
        return newHead