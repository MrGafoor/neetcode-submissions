class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        large=0

        for i in nums:
            if i-1 not in num:
                lon=0
                while (i+lon) in num:
                    lon+=1
                large=max(large,lon)
        return large
        