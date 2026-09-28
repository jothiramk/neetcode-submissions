class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time = time + 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                # print(f'processing {task}')
                #in the queue store the remaining freq for a task and a time for when it can be used again
                if abs(1+task) > 0:
                    pair = (1 + task,time+n)
                    q.append(pair)
                    # print(f'q value reamining task {pair[0]} nad {pair[1]}')
                    

            if q and  time == q[0][1]:
                poped_task = q.popleft()
                heapq.heappush(maxHeap,poped_task[0])
        
        return time

