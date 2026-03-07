#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)-1  
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if (target<nums[start] or target>nums[mid]):
                    start = mid + 1
                else:
                    end = mid -1
            else:
                if (target<nums[mid] or target>nums[end]):
                    end = mid -1
                else:
                    start = mid + 1  
        return -1
    
    # def search(self, nums: List[int], target: int) -> int:

    #     start = 0
    #     end = len(nums)
        
    #     while start < end:
    #         mid = (start + end) // 2
    #         if nums[mid] == target:
    #             return mid

    #         if nums[start] <= nums[mid]:
    #             if (target<nums[start] or target>nums[mid]):
    #                 start = mid + 1
    #             else:
    #                 end = mid
    #         else:
    #             if (target<nums[mid] or target>nums[end-1]):
    #                 end = mid
    #             else:
    #                 start = mid + 1  
    #     return -1


            
        
# @lc code=end

