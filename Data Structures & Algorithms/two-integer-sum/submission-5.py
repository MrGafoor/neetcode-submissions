class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tslist={}
        for i , n in enumerate(nums):
            tslist[n]=i
        for i , n in enumerate(nums) :
            diff=target-n
            if (diff in tslist) and i!=tslist[diff]:
                return [i,tslist[diff]]
        return []
