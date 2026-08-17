class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        print(digitToChar[2])
      
        res = []
        def dfs (i, combination):
            if len(combination) == len(digits):
                res.append(combination)
                return
# why there's no append or pop (similar to the other backtracking approaches) it's because strings are immutable. Everytime the call is made to the backtrack method, python creates a new string so when the method returns up the stack, the caller still has the original string without the concatenated letter.
            for ch in digitToChar[int(digits[i])]:
                dfs(i+1, combination + ch)
            
        if digits:
            dfs(0, "")
        return res