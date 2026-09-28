class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        print(f'dp initial {dp}')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                print(f'dp upadte first  {dp}')

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
                print(f'dp upadte second {dp}')
        return dp[0]