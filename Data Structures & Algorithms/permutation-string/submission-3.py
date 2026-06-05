class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False
        s1 = sorted(s1)

        for r in range(m, n + 1): # O(N)
            w = s2[r - m: r]

            if sorted(w) == s1: return True # O(NlogN)
        
        return False