from bisect import bisect_left
from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        l, r = 0, m - 1

        while True:
            mid = l + (r - l) // 2
            idx = half - mid - 2


            A_right = nums1[mid + 1] if mid + 1 < m else inf
            A_left = nums1[mid] if mid >= 0 else -inf
            B_right = nums2[idx + 1] if idx + 1 < n else inf
            B_left = nums2[idx] if idx >= 0 else -inf

            # if max(A_left, B_left) <= min(A_right, B_right):
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return max(A_left, B_left)

            elif A_left > B_right:
                r = mid - 1
            else:
                l = mid + 1