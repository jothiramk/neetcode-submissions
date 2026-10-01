# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #check solution 1, which is using additonal space but better optmizing the list we created instead of traversing the list all over
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_list = []
        curr = head
        while curr:
            nodes_list.append(curr)
            curr = curr.next
        

        size = len(nodes_list)
        curr = head
        prev = ListNode(-1)
        i = 0
        while curr:
            #remove the node
            if i == size-n:
                prev.next = curr.next        
                if i == 0:
                    head = prev.next
                break
            prev = curr
            curr = curr.next
            i+=1
        
        return head
            