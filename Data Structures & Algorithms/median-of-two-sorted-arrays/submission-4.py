class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=len(nums1)
        b=len(nums2)
        sum=[]
        for i in nums1:
            sum.append(i)
        for j in nums2:
            sum.append(j)
        sum.sort()
        print (sum)
        s=len(sum)
        if s%2 !=0:
            mid=(s)//2
            return sum[mid]
        else:
            mid=((0+(s))//2)
            return (sum[mid]+sum[(mid-1)])/2

        
       

        