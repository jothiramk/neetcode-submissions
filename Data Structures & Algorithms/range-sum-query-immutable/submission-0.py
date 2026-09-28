class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0
        for num in nums:
            total+= num
            self.prefix_sum.append(total)


    def sumRange(self, left: int, right: int) -> int:
        total_sum = self.prefix_sum[right]
        prefix_sum = self.prefix_sum[left-1] if left>0 else 0
        return total_sum - prefix_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)