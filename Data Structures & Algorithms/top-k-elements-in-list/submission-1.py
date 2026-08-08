class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt={}
        arr=[[] for i in range(len(nums)+1)]
        for i in nums:
            dt[i]=1+dt.get(i,0)
        for i,cnt in dt.items():
            arr[cnt].append(i)
        res=[]
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                res.append(n)  
                if len(res)==k:
                    return res      
              