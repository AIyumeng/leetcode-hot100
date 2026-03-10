#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:

        if n == 0:
            return 1
        elif n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):

            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[-1]


# @lc code=end
