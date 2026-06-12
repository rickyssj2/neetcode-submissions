from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapify(maxheap)

        while len(maxheap) > 1:
            x, y = heappop(maxheap), heappop(maxheap)
            if x != y:
                heappush(maxheap, x - y)
        return 0 if not maxheap else -maxheap[0]