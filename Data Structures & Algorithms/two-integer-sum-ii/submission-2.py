class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        res = []
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                res = [i+1,j+1]
                return res
            elif sum > target:
                j-=1
            else:
                i+=1
        return res
            