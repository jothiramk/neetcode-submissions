class Solution:
    def scoreOfString(self, s: str) -> int:
        scores = []
        for ch in s:
            scores.append(ord(ch))
        
        total = 0
        for i in range(1,len(scores)):
            total += abs(scores[i] - scores[i-1])
        
        return total