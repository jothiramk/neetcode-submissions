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
                #here essentiatly we are reducing the feq of task by 1, but since we use max value(storing negative values, we are doing +1 instead)
                cnt = 1 + heapq.heappop(maxHeap)
                
                #in the queue store the remaining freq for a task and a time for when it can be used again
                if cnt:
                    pair = (cnt,time+n)
                    q.append(pair)
                    
                    

            if q and  time == q[0][1]:
                poped_task = q.popleft()
                heapq.heappush(maxHeap,poped_task[0])
        
        return time

