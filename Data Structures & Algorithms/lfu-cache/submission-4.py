
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        # Key -> frequency
        # Example: {10: 2, 20: 1}
        self.key_to_freq = {}

        # Frequency -> OrderedDict of {key: value}
        # Example: {
        #     1: OrderedDict({20: 200, 30: 300}),
        #     2: OrderedDict({10: 100})
        # }
        # this is equivalent to the lru map in lru cache problem
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        # Find the current frequency of this key
        freq = self.key_to_freq[key]
        value = self.freq_to_keys[freq][key]

        self._increment_frequency(key)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_freq:
            # Get the current frequency of the existing key
            freq = self.key_to_freq[key]
            # Update its value in the corresponding frequency bucket
            self.freq_to_keys[freq][key] = value
            self._increment_frequency(key)
            return

        if len(self.key_to_freq) >= self.capacity:
            # Get the OrderedDict corresponding to the minimum frequency.
            # This bucket contains all keys with the lowest frequency.
            lru_keys = self.freq_to_keys[self.min_freq]
            evict_key, evict_value = lru_keys.popitem(last=False)
            
            # Remove the evicted key's frequency mapping as well.
            # Otherwise, key_to_freq would contain a stale entry.
            del self.key_to_freq[evict_key]
            
            #Clean code,  If the frequency bucket is now empty, remove it.
            if not lru_keys:
                del self.freq_to_keys[self.min_freq]

        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.min_freq = 1

    def _increment_frequency(self, key: int) -> None:
        # Get the current frequency of the key
        freq = self.key_to_freq[key]

        # Retrieve value before removing key
        value = self.freq_to_keys[freq][key]
        # Remove the key from its current frequency bucket
        del self.freq_to_keys[freq][key]
        # Check whether the current frequency bucket is now empty
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            # If this was the minimum frequency bucket increment min_freq because this key was its last member.
            if freq == self.min_freq:
                self.min_freq += 1

        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq][key] = value
