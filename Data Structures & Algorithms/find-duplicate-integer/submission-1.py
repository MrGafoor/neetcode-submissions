class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[c]:
                return nums[i]
            c+=1
        return 0
