#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(first):
            if first == n:
                res.append(nums[:])
                return

            used = set()  # 本层已经用过的数
            for i in range(first, n):
                if nums[i] in used:
                    continue

                used.add(nums[i])
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res

        
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         n = len(nums)
#         used = [False] * n

#         def dfs(path):
#             if len(path) == n:
#                 res.append(path.copy())
#                 return
#             for i in range(n):
#                 if used[i]:
#                     continue
#                 if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
#                     continue
#                 used[i] = True
#                 path.append(nums[i])
#                 dfs(path)
#                 path.pop()
#                 used[i] = False

#         dfs([])
#         return res
            

        
# @lc code=end

