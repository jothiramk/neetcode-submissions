class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = list(freq.values())
        heapq.heapify_max(max_heap)

        q = deque()
        time = 0
        

        while max_heap or q:
            time += 1
            if max_heap:
                curr_task = heapq.heappop_max(max_heap)
                remaining_task = curr_task - 1

                if remaining_task > 0:
                    q.append((remaining_task,time+n))
            
            if q and time == q[0][1]:
                curr_task = q.popleft()
                heapq.heappush_max(max_heap,curr_task[0])


        return time
        
       