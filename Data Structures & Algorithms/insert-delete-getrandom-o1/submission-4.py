class RandomizedSet:

    def __init__(self):
        self.container_map = {}
        self.container_list = []

    def insert(self, val: int) -> bool:
        if val in self.container_map:
            return False
        self.container_map[val] = len(self.container_list)
        self.container_list.append(val)
        return True

#container_list = [10, 20, 30]
#container_map = {10: 0, 20: 1, 30: 2}
#remove 10 - we should update the value of 30 to be at index of the item we are deleing
#container_map = {20: 1, 30: 0}

    def remove(self, val: int) -> bool:
        if val not in self.container_map:
            return False

        idx = self.container_map[val]
        last = self.container_list[-1]

        #the goal is to move the value to be removed to end(last) of list and then pop the last element, 
        #and also update the map with the new index of the value at the end(last)

        # Move the last element into val's position.
        self.container_list[idx] = last
        self.container_map[last] = idx

        # Remove the final element and val from the map.
        self.container_list.pop()
        del self.container_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.container_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()