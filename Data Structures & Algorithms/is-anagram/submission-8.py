class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        
        for i in range(len(t)):
            if t[i] not in counter_s:
                return False
            elif t[i] in counter_s:
                counter_s[t[i]] -= 1

        for value in counter_s.values():
            if value != 0:
                return False

        return True


