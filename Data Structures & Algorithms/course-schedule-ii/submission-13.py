class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req_maps = defaultdict(list)
        for crs,pre in prerequisites:
            pre_req_maps[crs].append(pre)
        
        result = []
        no_pre_req = set()
        cycle = set()


        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in no_pre_req:
                return True

            cycle.add(crs)

            for pre in pre_req_maps[crs]:
                if not dfs(pre):
                    return False
            no_pre_req.add(crs)
            result.append(crs)
            # print(f'updating result {result}')
            cycle.remove(crs)
            return True

        for crs in range(numCourses):
            if crs not in no_pre_req:
                if not dfs(crs):
                    return []

        return result