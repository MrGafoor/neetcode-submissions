class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        sublist=[]
        def dfs(i):
            if sublist in res:
                return
            if i==len(nums):
                res.append(sublist.copy())
                return 
            sublist.append(nums[i])
            dfs(i+1)
            sublist.pop()
            dfs(i+1)
            


        dfs(0)
        return res           