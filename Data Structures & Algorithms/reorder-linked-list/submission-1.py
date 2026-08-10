# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = None

        if head is None or head.next is None:
            # print(f'break condition')
            return
        
        curr = head
        prev= None
        
        while curr.next:
            prev = curr
            curr = curr.next

        tail = prev.next
        prev.next=None

        print(f'{curr.val} {prev.val} {tail.val}')
        curr = head
        temp_node = curr.next
        curr.next=tail
        tail.next=temp_node

        # print(f'{temp_node.val}')
        # temp_node1 = temp_node
        # while temp_node1:
        #     print (f'temp {temp_node1.val}')
        #     temp_node1 = temp_node1.next
        self.reorderList(temp_node)
