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

        prev = None
        head = None

        while sum :
            val = sum%10
            new_node=ListNode(val)
            new_node.next = prev
            prev=new_node
            head= new_node
            sum = sum // 10
            print(f'{val} {sum}')

        #reverse the list
        curr = head
        prev= None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
