class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_volume = -math.inf
        while i < j:
            volume = min(heights[i],heights[j]) * (j-i)
            max_volume = max(volume, max_volume)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_volume
        