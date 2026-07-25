class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct,window={},{}
        for c in range(len(t)):
            ct[t[c]]= 1+ct.get(t[c],0)
        have,need=0,len(t)
        res,reslen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in t and window[s[r]] <= ct[s[r]]:
                have+=1
            while have == need:
                if (r-l+1) < reslen:
                    reslen= r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in t and window[s[l]] < ct[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen != float("infinity") else ""