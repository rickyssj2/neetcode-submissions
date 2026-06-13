from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = [] # maxheap
        self.right = [] # minheap

    def addNum(self, num: int) -> None: # O(logN)
        if self.right and self.right[0] <= num:
            heappush(self.right, num)
            num = heappop(self.right)
            
        heappush(self.left, -num)

        # balance
        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))

    def findMedian(self) -> float: # O(1)
        n = len(self.left) + len(self.right)
        if n & 1:
            return -self.left[0]
        
        return (-self.left[0] + self.right[0]) / 2


    # what if add calls == findMedian call?
    # Optimizing for common case
        
        