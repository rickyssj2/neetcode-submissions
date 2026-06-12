from bisect import insort
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums.sort(reverse=True) # O(NlogN)

    def add(self, val: int) -> int:
        insort(self.nums, val, key=lambda x: -x) # O(N)
        return self.nums[self.k - 1]


    # Q, N TC => QN + NlogN
