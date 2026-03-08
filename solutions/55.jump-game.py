#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        max_l = 0
        for i in range(n):
            if max_l >= i:
                max_l = max(max_l, i+nums[i])
            else:
                break
            
        return max_l>=n-1
            

        
# @lc code=end

