class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dis={i:[] for i in range(numCourses)}
        for crs , pre in prerequisites:
            dis[crs].append(pre)
        vis,cycle=set(),set()
        res=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True
            cycle.add(crs)
            for pre in dis[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            vis.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs)==False:
                return[]
        return res
















