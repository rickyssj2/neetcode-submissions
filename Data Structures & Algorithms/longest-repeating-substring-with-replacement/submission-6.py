class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # only 1 unique char, but I can replace k mismatches
        # A: 4, B:1

        # AAABCAA k = 2

        # BIAS: We never change char at l or r
        n = len(s)
        ans = 0
        for l in range(n):
            kk = k
            freq = defaultdict(int)
            F = 0
            for r in range(l, n):
                freq[s[r]] += 1
                F = max(F, freq[s[r]])
                R = (r - l + 1) - F
                if R <= k:
                    ans = max(ans, r - l + 1)
        return ans

        # l ....... r
        # freq = {
        #     A: a
        #     B: b
        #     .
        #     .
        #     .
        #     .
        #     Z: z
        # }

        # # I DON'T WANT TO CHANGE THE MOST FREQ ELEMENT
        # K: k <- most frequent

        # L: l

        # k ≥ for all other freqs

        # # HOW MANY REPLACEMENTS ARE REQ?
        # R = W - F
        # R ≤ k
        # where F is the freq of most freq element