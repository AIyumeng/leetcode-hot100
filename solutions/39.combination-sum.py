#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])  # 必须复制
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])  # 注意这里是 i
                path.pop()

        dfs(0, [], 0)
        return res

        
        
    
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
    #     o = [[]]
    #     for c in candidates:
    #         new_o = []
    #         for oo in o:
    #             while sum(oo)<=target:   
    #                 new_o.append(oo)
    #                 oo = oo + [c]

    #         o = new_o
    #     new_o = []
    #     for oo in o:
    #         if sum(oo)==target:
    #             new_o.append(oo)

    #     return new_o




# @lc code=end

