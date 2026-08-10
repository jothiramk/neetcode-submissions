# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '',''

        while l1:
            num1+=str(l1.val)
            l1=l1.next

        while l2:
            num2+=str(l2.val)
            l2=l2.next
        
        sum =  int(num1[::-1]) + int(num2[::-1])
        print (f'sum is {sum}')

        if sum == 0:
            return ListNode(0)

        
        dummy = ListNode(0)
        curr = dummy 

        while sum :
            val = sum%10
            curr.next = ListNode(val)
            curr = curr.next
            sum = sum // 10
            # print(f'{val} {sum}')

        
        return dummy.next
