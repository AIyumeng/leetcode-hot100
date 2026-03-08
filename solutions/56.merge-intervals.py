#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        intervals = intervals[::-1]

        o = [intervals.pop()]

        while intervals:
            cur = intervals.pop()
            if cur[0]>o[-1][1]:
                o.append(cur)

            else:
                temp = o.pop()

                o.append([temp[0],max(cur[1], temp[1])])

        return o


        

# @lc code=end

