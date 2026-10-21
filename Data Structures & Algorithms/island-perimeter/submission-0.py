class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        visited = set()
        def dfs(r,c):
            #if it the bounday contions we count one towards the perimeter
            nonlocal perimeter
            if (r,c) in visited:
                return 0
            if min(r,c) < 0 or r>=rows or c >=cols or grid[r][c] == 0:
                # return 1
                perimeter+=1
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            # perimeter += dfs(r+1,c)
            # perimeter += dfs(r-1,c)
            # perimeter += dfs(r,c+1)
            # perimeter += dfs(r,c-1)
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)