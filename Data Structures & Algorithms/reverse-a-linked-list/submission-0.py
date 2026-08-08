# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr == None:
            return None
        head = None
        while curr:
            new_node = ListNode(curr.val)
            new_node.next= head
            head = new_node
            curr = curr.next
        return head
