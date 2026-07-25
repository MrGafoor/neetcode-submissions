class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        fresh=0
        q=deque()
        time=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c] ==2:
                    q.append([r,c])
        dir=[[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dir:
                    ro=dr+r
                    co=dc+c
                    if(ro<0 or ro==row or co<0 or co==col or
                        grid[ro][co]!= 1):
                        continue
                    q.append([ro,co])
                    grid[ro][co]=2
                    fresh-=1
            time+=1
       
        return time if fresh== 0 else -1