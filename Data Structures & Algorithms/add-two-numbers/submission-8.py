# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = 0 , 0
        i = 1
        while l1:
            num1 += (l1.val*i)
            i*=10 
            l1= l1.next

        i = 1
        while l2:
            num2 += (l2.val*i)
            i*=10 
            l2= l2.next
        
        target = num1 + num2
        if target == 0:
            return ListNode(0)
        head = ListNode(-1)
        curr = head
        while target:
            val = target%10
            target = target//10
            newNode = ListNode(val)
            curr.next = newNode
            curr = newNode

        return head.next