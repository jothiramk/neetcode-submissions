class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        visited = set()
        #first find all treasures and enque them
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        # print(len(q))
        
        while q:
            r, c = q.popleft()
            # print(f'processing {r} and {c}')
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if min(nr,nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == -1 or (nr,nc) in visited:
                    continue
                grid[nr][nc] = grid[r][c]+1
                q.append((nr,nc))
                visited.add((nr,nc))


        