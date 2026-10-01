# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
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
            print(f'{curr.val} and {prev.val}')
            #remove the node
            if i == size-n:
                prev.next = curr.next
                print(f'inside if {curr.val} and {prev.val}')
                if i == 0:
                    head = prev.next
                break
            prev = curr
            curr = curr.next
            i+=1
        
        # print(head)
        # if not head:
        #     head = prev.next
        return head
            