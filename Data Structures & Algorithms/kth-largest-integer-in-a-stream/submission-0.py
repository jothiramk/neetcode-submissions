class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.k = k



    def add(self, val: int) -> int:
        self.sorted_nums.append(val)
        self.sorted_nums.sort()
        size = len(self.sorted_nums)
        return self.sorted_nums[size-self.k]
