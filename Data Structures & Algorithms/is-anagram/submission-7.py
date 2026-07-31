class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_dict = {}
        for ch in s:
            if ch in counter_dict:
                counter_dict[ch] += 1
            else:
                counter_dict[ch] = 1

        for ch in t:
            if ch in counter_dict:
                counter_dict[ch] -= 1
            else:
                return False

        for k in counter_dict:
            if counter_dict[k] != 0:
                return False
        
        return True



