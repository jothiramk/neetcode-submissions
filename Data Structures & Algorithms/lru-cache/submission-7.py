from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_map = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.lru_map:
            return -1
        
        self.lru_map.move_to_end(key,last=True)
        return self.lru_map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lru_map:
            self.lru_map.move_to_end(key, last = True)
        
        self.lru_map[key] = value

        if len(self.lru_map) > self.capacity:
            self.lru_map.popitem(last = False)
