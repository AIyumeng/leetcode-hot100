#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        left_max = right_max = 0
        res = 0

        while left <= right:

            if left_max < right_max:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1

        return res







        
# @lc code=end

