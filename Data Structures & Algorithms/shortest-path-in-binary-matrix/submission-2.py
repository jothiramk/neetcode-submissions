class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        # 8 directional, can move diagonally as well 
        direction = [[1,0],[-1,0],[0,1],[0,-1],[-1, -1], [-1, 1], [1, -1], [1, 1]]
        visited = set()
        q = deque()
        q.append((0,0))
        visited.add((0,0))

        length = 1

        while q:
            for j in range(len(q)):
                r, c = q.popleft()
                if r == rows-1 and c == cols-1:
                    return length

                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc]==1 or (nr,nc) in visited:
                        continue

                    q.append((nr,nc))
                    visited.add((nr,nc))
            length+=1
        return -1

                
 
