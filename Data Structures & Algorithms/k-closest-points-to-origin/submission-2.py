from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapify(maxheap := [(-x**2 - y**2, (x, y)) for x, y in points])
        while len(maxheap) > k: heappop(maxheap)
        return [[x, y] for _, (x, y) in maxheap]
