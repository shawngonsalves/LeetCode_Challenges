class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}

        visit = set()
        cycle = set()
        res = []
        for crs,pre in prerequisites:
            adjList[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False

            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
                

        
