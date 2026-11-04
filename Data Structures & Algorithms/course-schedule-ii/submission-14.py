class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create an adj list
        pre_req_map = defaultdict(list)
        for crs,pre in prerequisites:
            pre_req_map[crs].append(pre)
        res = []
        # 1 -> 4 , 2-> 4, 3 -> 1, 3 ->2
        # 4 -> 1 -> 2 -> 3
        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
                        
            cycle.add(crs)
            for prereq in pre_req_map[crs]:
                if not dfs(prereq):
                    return False
            #meaning no pre-req
            visited.add(crs)
            res.append(crs)
            cycle.remove(crs)
            # print(visited)
            return True


        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        return res