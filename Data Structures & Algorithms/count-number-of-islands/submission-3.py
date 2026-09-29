class Solution:
    def dfs (self, grid: List[List[str]], r : int, c : int,rows : int, cols : int , visited : set()) -> int:
        if r<0 or c <0 or r>=rows or c>=cols or grid[r][c]=="0" or (r,c) in visited:
            return 

        visited.add((r,c))
        self.dfs(grid,r+1,c,rows,cols,visited)
        self.dfs(grid,r-1,c,rows,cols,visited)
        self.dfs(grid,r,c+1,rows,cols,visited)
        self.dfs(grid,r,c-1,rows,cols,visited)
        

        return 
        

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    self.dfs(grid,r,c,rows,cols,visited)
                    islands+=1
        
        return islands