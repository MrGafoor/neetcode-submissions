class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        alt,pef=set(),set()
        def dfs(r,c,vis,prevh):
            #
            if(r<0 or r==row or c<0 or c==col or (r,c) in vis 
                or prevh>heights[r][c]):
                return
            vis.add((r,c))
            dfs(r+1,c,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])

        for r in range(row):
            dfs(r,0,pef,heights[r][0])
            dfs(r,col-1,alt,heights[r][col-1])
        for c in range(col):
            dfs(0,c,pef,heights[0][c])
            dfs(row-1,c,alt,heights[row-1][c])

        res=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pef and (r,c) in alt:
                    res.append([r,c])
        return res