class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, maxright, l, r, water = height[0], height[(n := len(height)) - 1], 0, n - 1, 0
        while l < r:
            if height[l] < height[r]: water, maxleft = water + max(0, min(maxleft, maxright) - height[l]), max(maxleft, height[(l := l + 1)])
            else: water, maxright = water + max(0, min(maxleft, maxright) - height[r]), max(maxright, height[(r := r - 1)])
        return water