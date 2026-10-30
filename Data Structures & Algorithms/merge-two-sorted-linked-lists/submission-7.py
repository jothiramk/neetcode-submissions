# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sorted_head = ListNode()
        temp_head = sorted_head
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp_head.next = list1
                temp_head = list1
                list1 = list1.next
            else:
                temp_head.next = list2
                temp_head = list2
                list2 = list2.next
        #append either of the remaining list to the temp head
        temp_head.next = list1 or list2
            

        return sorted_head.next

            
