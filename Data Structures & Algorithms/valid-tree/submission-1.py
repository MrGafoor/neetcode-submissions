class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dit={i:[] for i in range(n) }
        for n1,n2 in edges:
            dit[n1].append(n2)
            dit[n2].append(n1)
        
        visit=set()
        def dfs(i, prev):
            if i in visit:
                return False
            if n==0:
                return True
            visit.add(i)
            for j in dit[i]:
                if prev == j:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n == len(visit)
        