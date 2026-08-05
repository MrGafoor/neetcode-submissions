class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ga=defaultdict(list)
        for i, n in enumerate(strs):
            co=[0]*26
            for c in n:
                co[ord(c)-ord('a')]+=1
            ga[tuple(co)].append(n)
        return list(ga.values())

