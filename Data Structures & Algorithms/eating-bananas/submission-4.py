class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, sum(piles)
        while l < r:
            if sum((p + (mid := l + (r - l) // 2) - 1) // mid for p in piles) <= h:   r = mid
            else:                                               l = mid + 1
        return r