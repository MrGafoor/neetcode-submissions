class Solution:
    def evalRPN(self, tockens: List[str]) -> int:
        st=[]
        if len(tockens)==1:
            return int(tockens[0])
        for r in range(len(tockens)):
            if tockens[r] == '+' :
                b=int(st.pop())
                a=int(st.pop())
                st.append(a+b)
            elif  tockens[r] =='-':
                b=int(st.pop())
                a=int(st.pop())
                st.append(a-b)
            elif tockens[r] =='*':
                b=int(st.pop())
                a=int(st.pop())
                st.append(a * b)
            elif tockens[r] =='/':
                b=int(st.pop())
                a=int(st.pop())
                st.append(int(a/b))
            else: 
                st.append(tockens[r])
        return st[0] 