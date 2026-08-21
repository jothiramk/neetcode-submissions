class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        visit = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r,c))

        def add_cell(r,c):
            if r<0 or c<0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == -1 :
                return 
            q.append((r,c))
            visit.add((r,c))
        
        dist = 0
        while q:
            for j in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    add_cell(nr,nc)
            dist+=1 
        


        
                    
                
                 
                 
                 
                
                

