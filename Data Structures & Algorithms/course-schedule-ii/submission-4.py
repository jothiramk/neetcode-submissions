class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = defaultdict(list)
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)
        
        cycle = set()
        path = set()
        output = []

        def dfs(crs):
            # print(f'prcoessing course {crs}')
            if crs in cycle:
                return False
            #check if the course is alrady taken - i.r no pre-req left for that particualr course, it would have been handled in the diff iteration
            if crs in path:
                return True
            
            cycle.add(crs)
            print(pre_req[crs])
            for pre in pre_req[crs]:
                if not dfs(pre):
                    return False
                
            cycle.remove(crs)
            path.add(crs)
            output.append(crs)   
            return True

        
        for crs in range(numCourses):
            if  dfs(crs) == False:
                return []
        
        return output
