class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False
        s1c = Counter(s1)
        s2c = Counter(s2[:m]) # defaultdict(int)

        for r in range(m, n): # O(N) m....n
            if s2c == s1c: return True # O(M)
            s2c[s2[r]] += 1
            s2c[s2[r - m]] -= 1
        if s2c == s1c: return True
        return False