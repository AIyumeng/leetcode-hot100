#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums:
    #         return [-1,-1]

    #     start = 0
    #     end = len(nums)-1
    #     while start<=end:
    #         mid = (start+end)//2
    #         if nums[mid]==target:
    #             break

    #         if nums[mid]<target:
    #             start = mid+1
    #         else:
    #             end = mid-1

    #     else:
    #         return [-1, -1]
    #     start, end = mid, mid
    #     while start>0 and nums[start-1]==target:
    #         start-=1
    #     while end<len(nums)-1 and nums[end+1]==target:
    #         end+=1

    #     return [start, end]
        

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 第一步：定义找左边界的函数
        def find_left():
            left, right = 0, len(nums) - 1
            # 循环条件：left <= right（覆盖所有情况）
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    # 即使等于target，也继续往左收缩，找第一个出现的位置
                    right = mid - 1
                else:
                    # 小于target，往右找
                    left = mid + 1
            # 循环结束后，left 是第一个 >= target 的位置，需要校验
            if left < len(nums) and nums[left] == target:
                return left
            return -1
        
        # 第二步：定义找右边界的函数
        def find_right():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    # 即使等于target，也继续往右收缩，找最后一个出现的位置
                    left = mid + 1
                else:
                    # 大于target，往左找
                    right = mid - 1
            # 循环结束后，right 是最后一个 <= target 的位置，需要校验
            if right >= 0 and nums[right] == target:
                return right
            return -1
        
        # 第三步：调用函数，返回结果
        left_idx = find_left()
        # 左边界不存在，直接返回[-1,-1]
        if left_idx == -1:
            return [-1, -1]
        right_idx = find_right()
        return [left_idx, right_idx]
    


# @lc code=end

