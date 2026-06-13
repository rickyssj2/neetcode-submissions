class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n & 1:
            idx = n // 2
            return self.nums[idx]
        
        return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2


    # what if add calls >> findMedian call?
        
        