class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = [0]
        visited = set()

        def dfs(r,c,count):
            if r < 0 or c <0 or r == rows or c == cols or grid[r][c] == 0  or (r,c) in visited:
                return 

            visited.add((r,c))
            # count +=1
            count[0]+=1
            # print(count)
            dfs(r+1,c,count)
            dfs(r-1,c,count)
            dfs(r,c+1,count)
            dfs(r,c-1,count)

            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_islands = [0] 
                    dfs(r,c,curr_islands)
                    # print(f'curr_islands is {curr_islands}')
                    islands = max(islands,curr_islands)
        
        return islands[0]