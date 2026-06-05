class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        tc = Counter(t)
        n = len(s)
        freq = Counter()
        l = 0
        ans = ""
        anslen = float('inf')
        for r in range(n): # N
            freq[s[r]] += 1 # My window might be valid

            # Shrink window is until invalid
            while all(val <= freq[key] for key, val in tc.items()):
                # Now my window is valid
                if anslen > (r - l + 1):
                    ans = s[l:r + 1]
                    anslen = len(ans)
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
        return ans