class Node:
    def __init__ (self,key,val,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lruMap = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.lruMap:
            #move the node the tail
            node = self.lruMap[key]
            self.remove(node)
            self.insertAtTail(node)

            return node.val
        else:
            return -1

    def remove(self, node):
        prev, next_node = node.prev, node.next
        prev.next = next_node
        next_node.prev = prev



    def insertAtTail(self, newNode):
        prev = self.right.prev
        self.right.prev=newNode
        newNode.next=self.right
        newNode.prev=prev
        prev.next=newNode
    
    def put(self, key: int, value: int) -> None:
        if key in self.lruMap:
            curr_node = self.lruMap[key]
            curr_node.val = value
            self.remove(curr_node)
            self.insertAtTail(curr_node)
        else:           
            #now store new in the DL at the tail -> L . NewNode. R

            newNode = Node(key,value)
            self.insertAtTail(newNode)          
            #insert into cache
            self.lruMap[key]=newNode

            if len(self.lruMap) > self.capacity:
                #remove from head, the LRU used cachce
                node_to_remove = self.left.next
                self.remove(node_to_remove)
                #remove the cache as well
                del self.lruMap[node_to_remove.key]