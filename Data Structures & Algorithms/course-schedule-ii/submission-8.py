from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list: course -> list of prerequisites
        preReq = defaultdict(list)
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        result = []
        cycle = set()  # Active DFS call stack (for cycle detection)
        visit = set()  # Fully processed courses (avoids duplicate processing)

        def dfs(crs: int) -> bool:
            if crs in cycle:
                return False  # Cycle detected!
            if crs in visit:
                return True   # Already processed and added to result

            cycle.add(crs)

            # Process all prerequisites first
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False  # Propagate cycle failure back up

            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)  # Post-order append: added AFTER all prerequisites

            return True

        # Run DFS on every course
        for crs in range(numCourses):
            if not dfs(crs):
                return []  # Return [] if any cycle exists

        return result