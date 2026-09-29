class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        visited = set()

        def dfs(r,c,visited):
            if min(r,c)<0 or r >= rows or c >=cols or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            counter = 0
            return 1 + dfs(r+1,c,visited) + dfs(r-1,c,visited) + dfs(r,c+1,visited) + dfs(r,c-1,visited)
            
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c,visited)
                    result = max(area,result)
        
        return result
