class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj={src:[] for src, dst in tickets}
        for a,b in tickets:
            adj[a].append(b)
        res=['JFK']
        def dfs(v):
            if len(res)==len(tickets)+1:
                return True
            if v not in adj:
                return False
            temp=list(adj[v])
            for i, ver in enumerate(temp):
                adj[v].pop(i)
                res.append(ver)
                if  dfs(ver): return True
                adj[v].insert(i,ver)
                res.pop()

            return False
        dfs('JFK')
        return res