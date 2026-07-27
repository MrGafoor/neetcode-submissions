class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dit={i:[] for i in range(n)}
        for n1,n2 in edges:
            dit[n1].append(n2)
            dit[n2].append(n1)
        visit=set()
        
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for j in dit[i]:
                dfs(j)
        count=0
        for i in range(n):
            if i not in visit:
                count+=1
                dfs(i)
       
        return count 
        
            