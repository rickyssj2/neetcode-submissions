from bisect import insort

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None: # O(N)
        insort(self.nums, num)

    def findMedian(self) -> float: # O(1)
        n = len(self.nums)
        if n & 1:
            idx = n // 2
            return self.nums[idx]
        
        return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2


    # what if add calls << findMedian call?
    # Optimizing for common case
        
        