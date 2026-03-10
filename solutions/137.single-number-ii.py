#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     count = [0] * 32
    #     for num in nums:
    #         for i in range(32):
    #             count[i] += (num >> i) & 1

    #     result = 0
    #     for i in range(32):
    #         if count[i] % 3 != 0:
    #             # 处理第31位（符号位）的负数情况
    #             if i == 31:
    #                 result -= (1 << i)
    #             else:
    #                 result |= (1 << i)

    #     return result
        

# @lc code=end

