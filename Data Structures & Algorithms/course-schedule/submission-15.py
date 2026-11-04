class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
     #BFS Approach
            graph = defaultdict(list)
            indegree = [0] * numCourses

            for course, prereq in prerequisites:
                graph[prereq].append(course)
                indegree[course] += 1

            queue = deque()

            for i in range(numCourses):
                if indegree[i] == 0:
                    queue.append(i)

            completed = 0

            while queue:
                node = queue.popleft()
                completed += 1

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            return completed == numCourses