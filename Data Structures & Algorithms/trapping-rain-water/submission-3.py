class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, maxright, l, r, water = height[0], height[(n := len(height)) - 1], 0, n - 1, 0
        while l < r:
            if height[l] < height[r]:
                water += max(0, min(maxleft, maxright) - height[l])
                l += 1
                maxleft = max(maxleft, height[l])
            else:
                water += max(0, min(maxleft, maxright) - height[r])
                r -= 1
                maxright = max(maxright, height[r])
        return water