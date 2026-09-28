class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #did not solve this, just saw the solution. the trick it find the max frequencies of a char and checking window - maxF < k and still a valid window
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
        