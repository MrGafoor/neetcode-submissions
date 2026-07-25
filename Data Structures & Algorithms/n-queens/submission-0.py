class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()#c sholud not be present in col
        posdia=set()#(r+c) sholud not be present in posdia
        negdia=set()#(r-c) sholud not be present in negdia
        res=[]
        board=[['.']*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdia or (r-c) in negdia:
                    continue
                col.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)

                col.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                board[r][c]="."

        

        backtrack(0)
        return res
        