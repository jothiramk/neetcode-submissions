class ListNode:
    def __init__(self,  key = 0, value=0, prev= None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev= self.left
        self.cache = {}

    def insert(self, node: ListNode):
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def remove(self, node: ListNode):

        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])        
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])
        

        if len(self.cache)> self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        




