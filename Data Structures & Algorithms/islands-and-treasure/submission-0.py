class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        vis=set()
        row,col=len(grid),len(grid[0])
        q=deque()

        def addroom(r,c):
            if (r<0 or r==row or c<0 or c==col or (r,c) in vis or grid[r][c]==-1):
                return
            vis.add((r,c))
            q.append([r,c])

        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append([r,c])
                    vis.add((r,c))
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            dist+=1

