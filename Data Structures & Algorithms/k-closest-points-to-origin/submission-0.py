from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = [(-x**2 - y**2, (x, y)) for x, y in points]
        heapify(maxheap)

        while len(maxheap) > k:
            heappop(maxheap)
        
        return [[x, y] for _, (x, y) in maxheap]
