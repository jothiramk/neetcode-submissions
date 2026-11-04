class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req_map = defaultdict(list)
        ingress = defaultdict(int)
        ingress = [0] * numCourses
        queue = deque()
        res = []

        for crs, pre in prerequisites:
            pre_req_map[pre].append(crs)
            ingress[crs]+=1
        print(f'prereq map {pre_req_map}')
        print(ingress)
        for i,count in enumerate(ingress):
            if count == 0:
                queue.append(i)
        print(queue)
        while queue:
            pre_req = queue.popleft()
            for crs_dep in pre_req_map[pre_req]:
                ingress[crs_dep] -=1
                if ingress[crs_dep] == 0:
                    queue.append(crs_dep)
            res.append(pre_req)
                
        return res if len(res) == numCourses else []

