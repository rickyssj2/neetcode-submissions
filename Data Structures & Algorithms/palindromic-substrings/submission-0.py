class Solution:
    def countSubstrings(self, s: str) -> int:
        t = "@*" + "*".join(list(s)) + "*$"
        p = [0] * len(t)

        for i in range(1, len(t) - 1):
            while t[i - p[i]] == t[i + p[i]]:
                p[i] += 1
        
        return sum((p[i] - 1) // 2 if i & 1 else p[i]//2 for i in range(len(p)))