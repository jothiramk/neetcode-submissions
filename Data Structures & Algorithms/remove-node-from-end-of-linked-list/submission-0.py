# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        size = len(nodes)
        target = size - n
        if target == 0:
            deleted_node = nodes[target]
            head = deleted_node.next
        else:
            deleted_node = nodes[target]
            prev_node = nodes[target-1]
            prev_node.next = deleted_node.next
        
        return head
        
        

        
