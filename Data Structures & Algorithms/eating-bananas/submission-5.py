class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return 0
        l=1
        r=0
        for j in piles:
            r=max(r,j)
        
        mini=r
        while l<r:
            m=(l+r)//2
            count=0
            for i in piles:
                count+=math.ceil(i/m)
            if count<=h:
                r=m
                
                mini=min(mini,m)
            elif count>h:
                l=m+1
            
        return mini

