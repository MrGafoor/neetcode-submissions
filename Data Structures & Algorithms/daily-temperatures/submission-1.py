class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        st=[]
        for i,t in enumerate(temp):
            while st and t > st[-1][-1]:
                sindx,stt=st.pop()
                res[sindx]=i-sindx
            st.append([i,t])
        return res

