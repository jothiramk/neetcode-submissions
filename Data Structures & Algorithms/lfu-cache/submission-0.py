class Node:
    def __init__(self, key, val, freq=1, next=None, prev=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = next
        self.prev = prev 

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        # Dictionaries to store left and right dummy nodes for each frequency bucket
        self.freq_left = {}
        self.freq_right = {}

    def _init_freq_bucket(self, freq: int):
        """Initializes dummy left and right nodes for a new frequency bucket."""
        left = Node(0, 0, freq)
        right = Node(0, 0, freq)
        left.next = right
        right.prev = left
        self.freq_left[freq] = left
        self.freq_right[freq] = right

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._update_node_freq(node)
        return node.val

    def remove(self, node):
        prev, next_node = node.prev, node.next
        prev.next = next_node
        next_node.prev = prev

    def insertAtTail(self, node):
        """Inserts the node at the tail (most recent) of its current frequency's list."""
        freq = node.freq
        if freq not in self.freq_left:
            self._init_freq_bucket(freq)
            
        right = self.freq_right[freq]
        prev = right.prev
        right.prev = node
        node.next = right
        node.prev = prev
        prev.next = node

    def _update_node_freq(self, node):
        freq = node.freq
        # 1. Remove from current frequency list
        self.remove(node)
        
        # If this bucket is now empty and was our min_freq, increment min_freq
        if freq == self.min_freq and self.freq_left[freq].next == self.freq_right[freq]:
            self.min_freq += 1
            
        # 2. Increment frequency and insert into the new frequency's tail
        node.freq += 1
        self.insertAtTail(node)

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_node_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                # Evict from the LFU list (starting at min_freq's head, which is the LRU item)
                lru_node = self.freq_left[self.min_freq].next
                self.remove(lru_node)
                del self.key_to_node[lru_node.key]

            # New nodes always start with a frequency of 1
            newNode = Node(key, value, freq=1)
            self.min_freq = 1
            self.insertAtTail(newNode)
            self.key_to_node[key] = newNode