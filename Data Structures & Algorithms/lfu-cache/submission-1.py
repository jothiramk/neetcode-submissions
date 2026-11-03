class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        # freq -> OrderedDict of {key: value} maintaining LRU order within that frequency
        self.freq_map = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # If key already exists, update value and bump frequency
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        # If at capacity, evict the least frequently used (and oldest) item
        if len(self.key_to_val) >= self.capacity:
            # popitem(last=False) pops the FIRST item in the OrderedDict (the LRU item for min_freq)
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        # Insert new key (always starts at frequency 1)
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_map[1][key] = value
        self.min_freq = 1  # A new item always resets min_freq to 1

    def _update_freq(self, key: int):
        freq = self.key_to_freq[key]
        val = self.key_to_val[key]
        
        # Remove from current frequency's OrderedDict
        del self.freq_map[freq][key]
        
        # If the bucket is now empty, clean it up and update min_freq if necessary
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        # Move to the next frequency bucket
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_map[new_freq][key] = val
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)