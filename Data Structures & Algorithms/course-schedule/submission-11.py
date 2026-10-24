class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build an adjacency list

        pre_req = defaultdict(list)
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)
        
        no_pre_req = set() 
        cycle = set()       

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in no_pre_req:
                return True
            
            cycle.add(crs)
        

            for pre_reqs in pre_req[crs]:
                if not dfs(pre_reqs):
                    return False
            no_pre_req.add(crs)
            cycle.remove(crs)
            return True
            
        
            

        for crs in range(numCourses):    
            if crs not in no_pre_req:
                if not dfs(crs):
                    return False
            
        return True

