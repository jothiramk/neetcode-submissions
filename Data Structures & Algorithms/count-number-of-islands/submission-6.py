class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):

            if min(r,c) < 0 or r>= rows or c>=cols or grid[r][c]=="0" or (r,c) in visited:
                return             
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(rows):
            for c in range (cols):
                # print(f'grid co {r} and {c} and val {grid[r][c]}')
                if grid[r][c] == "1" and (r,c) not in visited:
                    # print("finding island")
                    dfs(r,c)
                    res+=1
                    # print(visited)
        return res
                    