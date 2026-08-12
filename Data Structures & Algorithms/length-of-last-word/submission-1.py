class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        res = 0

        while j >= 0:
            if s[j].isalpha():
                res += 1
            elif res > 0:
                return res
            j -= 1

        return res