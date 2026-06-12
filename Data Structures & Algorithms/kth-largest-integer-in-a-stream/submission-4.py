from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapify(self.minheap) # O(N)

        while len(self.minheap) > k: # O(kLogN)
            heappop(self.minheap)

        # Now minheap has largest K elements

    def add(self, val: int) -> int:
        heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heappop(self.minheap)
        return self.minheap[0]

    # Q, N TC => Qlogk + N + kLogN
