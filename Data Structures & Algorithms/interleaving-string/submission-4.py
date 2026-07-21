from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,o = len(s1), len(s2), len(s3)
        if m + n != o: return False 

        # i means I split after index i

        # 2, 4 -> string
        # aa, ""

        # aabbbb
        @cache
        def dp(i, j):
            k = i + j
            if k == o:
                return True
            
            if i == m:
                return s2[j : n] == s3[k : o]
            if j == n:
                return s1[i : m] == s3[k : o]

            
            for ii in range(i, m):
                for jj in range(j, n):
                    kk = (ii + 1) + (jj + 1) 
                    if s1[i : ii + 1] + s2[j : jj + 1] != s3[k : kk] and\
                       s2[j : jj + 1] + s1[i : ii + 1] != s3[k : kk]:
                        continue
                        
                    if dp(ii + 1, jj + 1):
                        return True
            return False
        
        return dp(0, 0)
        