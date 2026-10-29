class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        queue = deque()
        res = 0
        for r in range(n):
            if s[r] not in queue:
                queue.append(s[r])
            else:
                while queue[0]!= s[r]:
                    queue.popleft()
                    l = l+1
                queue.popleft()
                l = l+1
                queue.append(s[r])
            res = max(res,r-l+1)
            # print(f'visitesd is {queue} and res is {res}')
        return res