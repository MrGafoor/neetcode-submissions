class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        close={
            ")" : "(",
            "]" :"[",
            "}" : "{"
        }
        for c in s:
            if c in close:
                if st and st[-1] == close[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if len(st) == 0 else False