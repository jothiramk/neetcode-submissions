class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # pre_req1 = {i : [] for i in range(numCourses)}
        # for crs,pre in prerequisites:
        #     pre_req1[crs].append(pre)
        
        pre_req = defaultdict(list)
        for crs,pre in prerequisites:
            pre_req[crs].append(pre)
        
        print(pre_req)
        cycle = set()

        def dfs(crs):
            # print(f'processing course {crs}')
            if crs in cycle:
                return False
            
            if pre_req[crs] == []:
                return True
            
            cycle.add(crs)
            # print(f'adding {crs} cycle {cycle}')
            for pre in pre_req[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            # print(f'removing {crs} visited {visited}')
            pre_req[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            
        
        return True