class MedianFinder:
    
    def __init__(self):
        self.small,self.large=[],[]    

    def addNum(self, num: int) -> None:
        #adding num to correct list in the two arrays
        if self.large and num>self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1*num)

        #balancing arrays
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]
        if len(self.small) == len(self.large):
            return (-1*self.small[0]+self.large[0])/2
        
        