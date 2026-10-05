class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x = 0
        y = 0
        visited.add((x,y))

        for i in range(len(path)):
            # print(visited)
            if path[i] == 'N':
                y+=1
            if path[i] == 'S':
                y-=1
            if path[i] == 'E':
                x+=1
            if path[i] == 'W':
                x-=1
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False
        