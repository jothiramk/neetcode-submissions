class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twoSum(target, index):
            i = index
            j = len(nums)-1
            res = []
            while i < j :
                sum = nums[i] + nums[j]
                if sum == target:
                    temp_res = [nums[i],nums[j]]
                    res.append(temp_res)
                if sum > target:
                    j-=1
                else:
                    i+=1
            return res

        final_result = []
        for i in range(len(nums)):
            twoSumTarget = 0 - nums[i]
            result = twoSum(twoSumTarget,i+1)
            # print(result)
            for res in result:
                intermediate_result = [nums[i]]
                intermediate_result.extend(res)
                if intermediate_result not in final_result:
                    final_result.append(intermediate_result) 
                # print(f'inal_result is {final_result}')
        return final_result
