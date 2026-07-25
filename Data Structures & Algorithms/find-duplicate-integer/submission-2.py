class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        s2=0
        while True:
            slow=nums[slow]
            s2=nums[s2]
            if slow == s2:
                return s2
