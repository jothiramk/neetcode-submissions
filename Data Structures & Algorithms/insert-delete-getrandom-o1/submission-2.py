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


    def remove(self, val: int) -> bool:
        if val not in self.container_map:
            return False
        idx = self.container_map[val]
        print(f'del val is {val} and idx is {idx} and {self.container_list} and {self.container_map}')
        #update the values/indexex of the 2 elements that we are going to swap before the swap
        self.container_map[self.container_list[-1]] = self.container_map[val]
        #swap the idx with the last element in the list
        self.container_list[-1], self.container_list[idx] = self.container_list[idx],self.container_list[-1]
        
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