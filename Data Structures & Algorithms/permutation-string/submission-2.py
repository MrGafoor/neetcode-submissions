class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hash = [0] * 26

        m = len(s1)
        n = len(s2)

        count = 0
        l = 0
        r = 0

        for i in range(m):
            hash[ord(s1[i]) - ord('a')] += 1

        while r < n:

            # Add s2[r]
            if hash[ord(s2[r]) - ord('a')] > 0:
                count += 1

            hash[ord(s2[r]) - ord('a')] -= 1

            # Keep window size = m
            if r - l + 1 > m:

                hash[ord(s2[l]) - ord('a')] += 1

                if hash[ord(s2[l]) - ord('a')] > 0:
                    count -= 1

                l += 1

            # All characters of s1 matched
            if count == m:
                return True

            r += 1

        return False