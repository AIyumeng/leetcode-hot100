#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for i in range(1,len(nums)):
            num = num^nums[i]

        return num
        
# @lc code=end

