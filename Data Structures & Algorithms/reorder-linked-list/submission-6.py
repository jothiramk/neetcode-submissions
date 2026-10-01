# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findTail(self, head):
        if not head:
            return None, None   

        prev = None
        curr = head       
        while curr.next:
            prev = curr
            curr = curr.next           
        return prev, curr  # Returns (prev_to_tail, tail)

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
        while curr:         
            prev, tail = self.findTail(curr) #6,8
            if prev:
                prev.next = None
            nxt = curr.next # 4
            # print(f'curr is {curr.val}  and tail is {tail.val} and nxt is {nxt.val}')
            curr.next = tail # 2->8
            tail.next = nxt # 2 -> 8 ->4
            curr = tail.next # curr = 8        

        