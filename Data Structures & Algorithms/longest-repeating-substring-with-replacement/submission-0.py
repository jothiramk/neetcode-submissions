class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #did not solve this, just saw the solution. the trick it find the max frequencies of a char and then adding k, if it would still be a valid window
        L = 0
        count = {}
        res = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            while (R-L+1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res
        