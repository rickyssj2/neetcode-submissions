class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = deque()
        n = len(nums)
        # [5][4][2][1] 
        for i in range(k - 1):
            c = nums[i]
            while mq and mq[-1] < c:
                mq.pop()
            mq.append(c) # [2]
        ans = []
        for r in range(k - 1, n):
            c = nums[r]
            while mq and mq[-1] < c:
                mq.pop()
            mq.append(c) # [1]
            ans.append(mq[0])

            le = nums[r - k + 1]
            if mq[0] == le:
                mq.popleft() 
        return ans