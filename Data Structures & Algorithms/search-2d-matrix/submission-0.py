class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix), len(matrix[0])
        top,bot=0,r-1
        while top<=bot:
            m=(top+bot)//2
            if target < matrix[m][0]:
                bot=m-1
            elif target > matrix[m][-1]:
                top=m+1
            else:
                break
        mid=(top+bot)//2
        l,ro=0,c-1
        while l<=ro:
            n=(l+ro)//2
            if target < matrix[mid][n]:
                ro=n-1
            elif target > matrix[mid][n]:
                l=n+1
            else: 
                return True
        return False
        