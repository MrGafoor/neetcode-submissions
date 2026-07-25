class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                windows.remove(nums[l])
                l+=1
            if nums[r] in windows:
                return True
            windows.add(nums[r])
        return False