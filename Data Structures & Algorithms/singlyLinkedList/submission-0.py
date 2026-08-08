class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        counter = 0
        curr = self.head
        while curr != None:
            if counter == index:
                return curr.val
            counter += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        counter = 0
        curr = self.head
        prev = None
        #if the index to be removed is head
        if counter == index:
            self.head = curr.next
            return True

        while curr != None:
            if counter == index:
                prev.next = curr.next
                return True
            counter += 1
            prev = curr
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        return res