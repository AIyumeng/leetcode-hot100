#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        # dp[i][j] s[:i] p[:j]
        dp[0][0] = True
        for i in range(2,n+1):         
            dp[0][i] = dp[0][i-2] if p[i-1]=='*' else False

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    if p[j-2]=='.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2] or (dp[i-1][j] and s[i-1] == p[j-2])
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1]==p[j-1]

        return dp[-1][-1]

        # dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-2][j-2] or ...
        # dp[i-1][j] = dp[i-1][j-2] or dp[i-2][j-2] or ...

        # dp[i][j] =
        # dp[i][j-2] or 
        # (dp[i-1][j-2] and s[i-1]==p[j-2]) or 
        # (dp[i-2][j-2] and s[i-1]==p[j-2] and s[i-2]==p[j-2]) or
        # (dp[i-3][j-2] and s[i-1]==p[j-2] and s[i-2]==p[j-2] and s[i-3]==p[i-2]) or ...

        # dp[i-1][j] =
        # dp[i-1][j-2] or 
        # (dp[i-2][j-2] and s[i-2]==p[j-2]) or 
        # (dp[i-3][j-2] and s[i-2]==p[j-2] and s[i-3]==p[j-2]) or
        # (dp[i-4][j-2] and s[i-2]==p[j-2] and s[i-3]==p[j-2] and s[i-4]==p[i-2]) or ...


# @lc code=end

