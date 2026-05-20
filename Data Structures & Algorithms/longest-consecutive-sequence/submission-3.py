class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # sortedNums = [2, 3, 4, 4, 5, 10, 20]
        # sortedNumset = [2, 3, 4, 5, 10, 20]

        numset = list(set(nums))
        numset.sort()
        if not numset:
            return 0
            
        cur_l, longest = 1, 1

        for i in range(len(numset) - 1):
            if numset[i + 1] - numset[i] == 1:
                cur_l += 1
                longest = max(cur_l, longest)
            else:
                cur_l = 1
        return longest