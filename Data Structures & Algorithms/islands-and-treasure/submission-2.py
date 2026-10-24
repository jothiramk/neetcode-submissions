class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647
        q = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        

        while q:
            row,col,dist = q.popleft()

            for dr,dc in directions:
                nr = dr +row
                nc = dc +col
                
                if min(nr,nc) < 0 or nr >= rows or nc >=cols or grid[nr][nc]==-1 or grid[nr][nc]!= inf:
                    continue
                
                grid[nr][nc]=dist+1
                q.append((nr,nc,dist+1))

                


