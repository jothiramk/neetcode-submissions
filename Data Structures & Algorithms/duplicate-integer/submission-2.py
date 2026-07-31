class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter_set = set()
        for num in nums:
            if num not in counter_set:
                counter_set.add(num)
            else:
                return True
        return False
 

