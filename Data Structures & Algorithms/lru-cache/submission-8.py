class ListNode:
    def __init__ (self, key, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_map = { }
        self.dummy_head = ListNode(-1,0)
        self.dummy_tail = ListNode(-1,0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def remove(self,nodeToRemove):

        prev_node = nodeToRemove.prev
        next_node = nodeToRemove.next

        prev_node.next = next_node
        next_node.prev= prev_node
        
        
    def insertAtTail(self, newNode):
        
        prev_tail = self.dummy_tail.prev

        newNode.next = self.dummy_tail
        newNode.prev = prev_tail
        prev_tail.next = newNode
        self.dummy_tail.prev = newNode
        
        
    def get(self, key: int) -> int:
        
        if key not in self.lru_map:
            
            return -1

        nodeToRemove = self.lru_map[key]
        self.remove(nodeToRemove)
        self.insertAtTail(nodeToRemove)
        
        return self.lru_map[key].value
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru_map:
            self.remove(self.lru_map[key])

        newNode = ListNode(key,value)
        self.insertAtTail(newNode)
        self.lru_map[key] = newNode
        

        if len(self.lru_map) > self.capacity:
            
            self.lru_map.pop(self.dummy_head.next.key)
            self.remove(self.dummy_head.next)
            
            
