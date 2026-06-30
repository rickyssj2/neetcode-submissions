class Solution:
    def countSubstrings(self, s: str) -> int:
        # Transform string to handle even-length palindromes cleanly
        t = "@*" + "*".join(list(s)) + "*$"
        p = [0] * len(t)
        
        c, r = 0, 0 # Track both center and right boundary
        
        for i in range(1, len(t) - 1):
            mirror = 2 * c - i # Correct mirror formula
            
            if i < r:
                p[i] = min(r - i, p[mirror])
            
            # Expand around center i
            while t[i - (1 + p[i])] == t[i + (1 + p[i])]:
                p[i] += 1
                
            # Update center and right boundary if expanded past r
            if i + p[i] > r:
                c = i
                r = i + p[i]
                
        # Each element in p[i] directly maps to the number of valid palindromes
        return sum((val + 1) // 2 for val in p)
