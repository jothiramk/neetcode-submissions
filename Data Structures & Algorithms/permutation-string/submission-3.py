class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l = 0
        s1_list = sorted(s1)
        for r in range(len(s2)):
            if (r-l+1) == window_size:
                if s1_list == sorted(s2[l:r+1]):
                    return True
                else:
                    l = l + 1
        return False