class Solution:

    def dfs(self,crs : int, preReq : dict, visited : set) -> bool :
        if crs in visited:
            return False
        
        if preReq[crs] == []:
            return True

        visited.add(crs)

        #traverse all the pre reqs of crs:
        for pre in preReq[crs]:
            if not self.dfs(pre,preReq,visited):
                return False
        
        visited.remove(crs)
        preReq[crs] = []
        
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #first build an adj list of the course - preq
        preReq = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preReq[crs].append(pre)
            
        visited = set()
        
        #run a DFS on each course, to check if it has a cycle
        for crs in range(numCourses):
            if not self.dfs(crs,preReq,visited):
                return False
        
        return True