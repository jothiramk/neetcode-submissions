# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        sorted_head = ListNode()
        temp_head = sorted_head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp_head.next = curr1
                temp_head = curr1
                curr1 = curr1.next
            else:
                temp_head.next = curr2
                temp_head = curr2
                curr2 = curr2.next
        while curr1:
            temp_head.next = curr1
            temp_head = curr1
            curr1 = curr1.next
        
        while curr2:
            temp_head.next = curr2
            temp_head = curr2
            curr2 = curr2.next

        return sorted_head.next

            
