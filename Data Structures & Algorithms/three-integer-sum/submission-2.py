class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res =[]
        # print(f'numbers {numbers} and target is {target}')
        while left < right :
            sum = numbers[left]+numbers[right]
            # print(f'sum is {sum}')
            if sum == target:
                res.append([numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            templist = []
            target = 0 - num
            twoindex = self.twoSum(nums[i+1:],target)
            for pair in twoindex:
                res.append([num] + pair)
        return res
    



        