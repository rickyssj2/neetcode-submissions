class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False
        s1counter = Counter(s1)

        for r in range(m, n + 1): # O(N)
            w = s2[r - m: r]

            if Counter(w) == s1counter: return True # O(N)
        
        return False