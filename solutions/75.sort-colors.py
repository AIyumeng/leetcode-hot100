#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
            
#         num0, num1, num2 = count.get(0, 0), count.get(1, 0), count.get(2, 0)
        
#         i = 0
#         for _ in range(num0):
#             nums[i] = 0
#             i += 1
#         for _ in range(num1):
#             nums[i] = 1
#             i += 1
#         for _ in range(num2):
#             nums[i] = 2
#             i += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        left, middle, right = 0, 0, N-1

        while middle <= right:
            if nums[middle] == 0:
                # Swap left and middle, increment both indicies
                nums[left], nums[middle] = nums[middle], nums[left]
                left += 1
                middle += 1
            elif nums[middle] == 1:
                # Position is correct, move middle forward
                middle += 1
            else:
                # Swap middle with right and decrement right
                nums[middle], nums[right] = nums[right], nums[middle]
                right -= 1
        
        return nums
        
# @lc code=end

