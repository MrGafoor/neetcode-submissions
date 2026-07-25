class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        deq=deque()
        l,r=0,0
        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)
            while l > deq[0]:
                deq.popleft()
            if (r+1)>=k:
                res.append(nums[deq[0]])
                l+=1
            r+=1
        return res