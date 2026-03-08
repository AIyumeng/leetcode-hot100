#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        n = len(nums)
        sum = 0
        max_sum = -20000
        while cur < n:
            sum += nums[cur]
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
            
            cur += 1

        return max_sum
            

        
# @lc code=end

