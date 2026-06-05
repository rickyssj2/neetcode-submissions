class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = ans = F = 0
        freq = Counter()
        
        for r in range(n):
            freq[s[r]] += 1
            F = max(F, freq[s[r]])

            while (r - l + 1) - F > k: # F is an upper bound on true_max ≤ F
                freq[s[l]] -= 1
                F = max(freq.values())
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans