class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I will check ALL substrings

        n, ans = len(s), 0
        for l in range(n):
            ss = set()
            for r in range(l, n):
                ss.add(s[r])
                if (r - l + 1) == len(ss):
                    ans = max(ans, r - l + 1)
                else:
                    break
        return ans