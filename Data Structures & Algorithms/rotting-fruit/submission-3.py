class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh_fruit = 0
        #enque all the rotten fruits for us to fanout from
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh_fruit+=1
        minute = 0
        while q:
            spoilt = False
            for i in range(len(q)):
                r,c = q.popleft()
                # print(f'processng {r} and {c}')
                
                for dr,dc in directions:
                    nr, nc = r +dr, c+dc

                    if min(nr,nc) < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or grid[nr][nc]==0:
                        # print(f'skipping {nr} and {nc}')
                        continue
                    #append to queu only for a fresh fruit, which is spoilt in this round
                    q.append((nr,nc))
                    visited.add((nr,nc))
                    fresh_fruit-=1
                    spoilt = True
                    # print(f'appending spoilt in this cycle {nr} and {nc} and spolit {spoilt}')
            if spoilt:
                # print(f'inside minute')
                minute += 1
            # print(f'total time so far {minute}')
        return minute if fresh_fruit == 0 else -1



