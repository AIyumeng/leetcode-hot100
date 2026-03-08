#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(path,n):
            if len(path)==n:
                res.append(path.copy())
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(path,n)
                    path.pop()

        dfs([],len(nums))

        return res
# @lc code=end

