class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build an adjacency list

        pre_req = defaultdict(list)
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)
        
        visited = set() 
        cycle = set()       

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)
        

            for pre_reqs in pre_req[crs]:
                if not dfs(pre_reqs):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            return True
            
        
            

        for crs in range(numCourses):    
            if crs not in visited:
                if not dfs(crs):
                    return False
            
        return True

