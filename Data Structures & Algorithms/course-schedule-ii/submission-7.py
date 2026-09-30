class Solution:

    def dfs(self, crs: int, preReq : dict , result : list , visited : set, processed : set):
        #there is a cycle 
        if crs in visited:
            return False
        if crs in processed:
            return True
        
        visited.add(crs)

        for pre in preReq[crs]:
            if not self.dfs(pre,preReq,result,visited,processed):
                return False


        result.append(crs)
        processed.add(crs)
        visited.remove(crs)
        preReq[crs] = []
        
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        result = []
        visited = set()
        processed = set()
        #build a prereq map
        preReq = defaultdict(list)
        for crs,pre in prerequisites:
            preReq[crs].append(pre)

        for crs in range(numCourses):
           
           if not self.dfs(crs,preReq,result,visited,processed):
             return []
           
            
        
        return result