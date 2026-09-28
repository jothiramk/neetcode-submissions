class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1len = len(word1)
        w2len = len(word2)
        i, j = 0, 0
        res = []
        while i < w1len and j < w2len:
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1

        if i < w1len:
            res.append(word1[i:])
        elif j < w2len:
            res.append(word2[j:])
        
        return "".join(res)