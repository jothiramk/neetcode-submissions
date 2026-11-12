class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(list)
        ingress = [0] * numCourses
        for crs,pre in prerequisites:
            pre_req[pre].append(crs)
            ingress[crs]+=1

        print(pre_req)
        print(ingress)
        queue = deque()
        #enque all crs with ingress 0
        for i in range(len(ingress)):
            if ingress[i]==0:
                queue.append(i)
        
        while queue:
            cur_crs = queue.popleft()
            # print(f'cur_crs in {cur_crs}')
            for neigh in pre_req[cur_crs]:
                ingress[neigh]-=1

                if ingress[neigh]==0:
                    queue.append(neigh)

        for i in range(len(ingress)):
            if ingress[i]!= 0:
                return False
        return True


        