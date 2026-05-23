class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, n = [], len(height)
        curmax = 0
        for h in height:
            maxleft.append(curmax)
            curmax = max(curmax, h)

        maxright = []
        curmax = 0
        for h in reversed(height):
            maxright.append(curmax)
            curmax = max(curmax, h)
        maxright.reverse()

        water = [0] * n
        for i, h in enumerate(height):
            water[i] = max(water[i], min(maxleft[i], maxright[i]) - h)
        print(water)
        return sum(water)