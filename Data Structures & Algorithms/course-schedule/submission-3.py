from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()  # Currently on the call stack (Gray)
        visit = set()  # Fully processed & proven safe (Black)

        def dfs(crs: int) -> bool:
            if crs in cycle:
                return False  # Cycle detected
            if crs in visit:
                return True   # Already proven safe

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)  # Mark as safe instead of doing preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True