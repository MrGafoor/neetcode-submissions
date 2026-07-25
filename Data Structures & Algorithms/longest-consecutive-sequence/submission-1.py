class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        long=0
        for n in nums:
            if (n-1) not in numSet:
                large=0
                while (n+large) in numSet:
                    large+=1
                long=max(large,long)
        return long