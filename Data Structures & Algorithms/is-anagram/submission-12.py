class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False
        
        count_s = Counter(s)
        count_t = Counter(t)
        for key, value in count_s.items():
            if count_t[key]!=value:
                return False
            else:
                count_s[key]=0
        
        for key, value in count_s.items():
            if value != 0:
                return False
        
        return True

    