class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()        
        fresh_fruits = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_fruits += 1

        # print(f'fresh_fruits initial count {fresh_fruits}')
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        days = 0
        while q and fresh_fruits > 0:
            # print(f'len of q is {len(q)} and {days} and fresh_sruits are {fresh_fruits}')
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if min(nr,nc) <0 or nr >= rows or nc >= cols or grid[nr][nc]== 0 or grid[nr][nc] == 2:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh_fruits -= 1
                    # print(f'fresh_fruits after update count {fresh_fruits}')
        
            days += 1

        if fresh_fruits > 0:
            return -1
        return days



