class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build an adjaceny list of all neighbours
        visited = [False] * n
        src_map = defaultdict(list)
        dst_map = defaultdict(list)
        for src,dest in edges:
            src_map[src].append(dest)
            src_map[dest].append(src)
        
        print(src_map)
        print(dst_map)
        def dfs(i):
            if visited[i]:
                return 
            visited[i] = True
            #find neighbours of i and iterate again
            for neigh in src_map[i]:
                # print(neigh)
                dfs(neigh)
            
            return 1

        #start from island 0 and see if you can visit every other island
        count = 0
        for i in range(n):
            if visited[i] == False:
                count += dfs(i) 

        return count

