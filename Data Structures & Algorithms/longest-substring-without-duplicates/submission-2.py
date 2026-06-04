class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I will check ALL substrings
        def valid(ss):
            return len(ss) == len(set(ss))

        n, ans = len(s), 0
        for l in range(n):
            for r in range(l, n):
                if valid(s[l : r + 1]):
                    ans = max(ans, r - l + 1)
                else:
                    break
        return ans