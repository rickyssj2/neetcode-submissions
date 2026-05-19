from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        for key, val in Counter(nums).items():
            heappush(minheap, (val, key))
            if len(minheap) > k:
                heappop(minheap)
        return [key for val, key in minheap]