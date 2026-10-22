class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build an adjacency list
        prereq_map = defaultdict(list)
        for crs,pre in prerequisites:
            prereq_map[crs].append(pre)
        
        print(dict(prereq_map))

        visited = set()
        cycle = set()

        def dfs(crs):
            # print(f'processing {crs}')
            if crs in cycle:
                return False
            
            if crs in visited:
                return True

            cycle.add(crs)
            

            for prereq in prereq_map[crs]:
                if not dfs(prereq):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            # print(f'ia ma here {crs} and {cycle} and {visited}')
            return True

        for crs in range(numCourses):
            if crs not in visited:
                if not dfs(crs):
                    return False
        
        return True
