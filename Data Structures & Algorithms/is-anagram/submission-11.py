class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurances = Counter(s)
        if len(s)!=len(t):
            return False
        print(occurances)
        for ch in t:
            occurances[ch]-=1
        
        for value in occurances.values():
            if value > 0:
                return False
        
        return True