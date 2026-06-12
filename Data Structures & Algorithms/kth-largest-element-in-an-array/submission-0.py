from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(minheap := nums)
        while len(minheap) > k: heappop(minheap)
        return minheap[0]