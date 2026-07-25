class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        a=len(nums)-k
        while a>0:
            heapq.heappop(nums)
            a-=1
        return heapq.heappop(nums)