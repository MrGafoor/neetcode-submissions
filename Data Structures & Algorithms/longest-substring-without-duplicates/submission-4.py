class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=[-1]*256
        l,r=0,0
        leng=0
        while(r<len(s)):
            indx=(ord(s[r])-ord('a'))
            if(arr[indx]!=-1):
                if (arr[indx]>=l):
                    l=arr[indx]+1
            maxlen=r-l+1
            leng=max(leng,maxlen)
            arr[indx]=r
            r+=1
        return leng