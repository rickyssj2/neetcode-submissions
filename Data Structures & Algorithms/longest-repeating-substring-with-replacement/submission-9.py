class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freq = Counter()
        ans = F = 0
        for r in range(n):
            freq[s[r]] += 1
            F = max(F, freq[s[r]])
            R = (r - l + 1) - F

            while R > k:
                freq[s[l]] -= 1
                F = max(freq.values())
                l += 1
                R = (r - l + 1) - F
            
            ans = max(ans, r - l + 1)
        return ans