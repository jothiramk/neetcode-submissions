# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        dummy = ListNode(0, head)
        left = dummy
        right = head
# Use two pointers so that the gap between them is exactly n.
# Move the right pointer n steps ahead first.

        while n > 0:
            right = right.next
            n -= 1
# Then move both pointers together.
# When the right pointer reaches the end, the left pointer will be just before the node we must remove.
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next