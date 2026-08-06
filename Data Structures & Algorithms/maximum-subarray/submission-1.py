class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane’s algorithm
# In a broader sense, Kadane’s algorithm is a textbook example of Greedy Optimization and Dynamic Programming. The pattern of traversing a sequence and deciding at each step whether to: [1, 2, 3]
# State_A: Keep accumulating/continuing the history.
# State_B: Throw away the history and restart the state at the current element.

        curr_sum = 0
        max_sum = nums[0]

        for num in nums:
            # most often the termination condition or the main logic should be the at the top
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + num
            max_sum = max(max_sum,curr_sum)

        return max_sum
        