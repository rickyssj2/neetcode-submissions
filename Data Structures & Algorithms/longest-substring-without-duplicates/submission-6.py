class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # VARIABLE SIZE SLIDING WINDOW
        # r increments while window is valid
        # when window becomes invalid, l keep incrementing
        # INVARIANT: window is always valid given the contraints, before updating my ans
        # r: what is the max valid window ENDING on me, l: starting from me
        def valid(r, l, freq):
            return (r - l + 1 == len(freq))
        n = len(s)
        freq = Counter()
        l = 0
        ans = 0
        for r in range(n): # N
            freq[s[r]] += 1 # My window might be invalid
            # Ensure window is valid
            while not valid(r, l, freq):
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            # Now my window is valid
            ans = max(ans, r - l + 1)
        return ans