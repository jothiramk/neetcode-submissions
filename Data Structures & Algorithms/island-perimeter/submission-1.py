class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(r, c):
            # If it hits a boundary or water, it contributes 1 to the perimeter
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            # If already visited, it contributes 0
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            
            count = 0
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
                    
        return 0