#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from math import inf

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        mid = (m + n) // 2
        # nums1 shorter than nums2
        # 二分
        start, end = 0, m  # 最多m, 最少0

        while start<=end:
            cur1 = (start + end) // 2
            cur2 = mid - cur1

            a = nums1[cur1 - 1] if cur1 > 0 else -inf
            b = nums1[cur1] if cur1 < m else inf
            c = nums2[cur2 - 1] if cur2 > 0 else -inf
            d = nums2[cur2] if cur2 < n else inf
            if a <= d and c <= b:
                break
            elif a > d:
                # cur1 大了
                end = cur1 - 1
            else:
                start = cur1 + 1

        # return a,b,c,d
        if (m + n) % 2 == 0:
            return (max(a, c) + min(b, d)) / 2
        else:
            return min(b, d)


# @lc code=end
