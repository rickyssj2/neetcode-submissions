class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, ans = 0, len(heights) - 1, 0

        while l < r:
            ans = max(ans, min(heights[l], heights[r]) * (r - l))

            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans