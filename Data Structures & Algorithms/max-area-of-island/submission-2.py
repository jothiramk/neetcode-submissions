class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or c <0 or r == rows or c == cols or grid[r][c] == 0  or (r,c) in visited:
                return 0

            visited.add((r,c))
            count = 1
            count += dfs(r+1,c)
            count += dfs(r-1,c)
            count += dfs(r,c+1)
            count += dfs(r,c-1)

            return count

            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_islands = dfs(r,c) 
                    # print(f'curr_islands is {curr_islands}')
                    islands = max(islands,curr_islands)
        
        return islands