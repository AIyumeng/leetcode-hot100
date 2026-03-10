#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def dfs(path, i):
            if i==n:
                res.append(path.copy())
                return

            dfs(path, i+1)
            dfs(path+[nums[i]],i+1)

        dfs([],0)

        return res


        
# @lc code=end

