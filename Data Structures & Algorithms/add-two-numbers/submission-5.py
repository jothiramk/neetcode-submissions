# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        n1 = 0
        n2 = 0
        i = 1
        while curr:
            n1 += (curr.val*i)
            curr= curr.next
            i=i*10
        
        curr = l2
        i = 1
        while curr:
            n2 += (curr.val*i)
            curr= curr.next
            i=i*10
        

        sum = n1 + n2
        
        head = None
        prev = None
        if sum == 0:
            return ListNode(0)
        while sum > 0:       
            rem = sum %10
            sum = sum//10
            new_node = ListNode(rem)
            # print(f'new_node val is {new_node.val}')
            if head is None:
                head = new_node
                temp_head = new_node
            else:
                temp_head.next = new_node
                temp_head = new_node
        return head