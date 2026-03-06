#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        results = []
        
        for i in range(n-2):
            start = i + 1
            end = n - 1
            target = 0 - nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue # 1
            if nums[start] + nums[start+1]>target:
                break
            if nums[end] + nums[end-1]<target:
                continue

            while start < end:
                if start > i+1 and nums[start] == nums[start-1]:
                    start +=1
                    continue # 2
                if end < n-1 and nums[end] == nums[end+1]:
                    end -=1
                    continue # 3
                cur = nums[start] + nums[end]
                if cur < target:
                    start += 1
                elif cur > target:
                    end -=1
                else:
                    results.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

        return results


        
# @lc code=end

