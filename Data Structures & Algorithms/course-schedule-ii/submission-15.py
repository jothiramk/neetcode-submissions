class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #BFS
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and calculate indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Add courses with no prerequisites
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        result = []

        # BFS - Kahn's Algorithm
        while queue:
            course = queue.popleft()
            result.append(course)

            # Process dependent courses
            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all courses were completed
        if len(result) == numCourses:
            return result

        return []