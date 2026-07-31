class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # print(f"sorted list {nums}")
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return True
        return False

