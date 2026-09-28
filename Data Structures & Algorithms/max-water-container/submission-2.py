class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        res = 0
        while i < j:
            vol = min(heights[i],heights[j])*(j-i)
            # print(f'volume is {vol} and {i} and {j}')
            res = max(res,vol)
            if heights[j]>heights[i]:
                i+=1
            else:
                j-=1
        
        return res
            