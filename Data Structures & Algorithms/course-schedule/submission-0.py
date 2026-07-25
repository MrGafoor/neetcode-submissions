class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        vis=set()
        def dfs(pre):
            if pre in vis:
                return False
            if premap[pre] == []:
                return True
            vis.add(pre)
            for i in premap[pre]:
                if not dfs(i): return False
            vis.remove(pre)
            premap[pre]=[]
            return True
            

        for pre in range(numCourses):
            if not dfs(pre): return False
        return True