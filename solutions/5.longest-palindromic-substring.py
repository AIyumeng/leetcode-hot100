#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     # s[start:end]
    #     start = 0
    #     end = 1
    #     n = len(s)
    #     a = []
    #     while True:
    #         if end == n:
    #             a.append((start, end))
    #             break
    #         if s[end] != s[start]:
    #             a.append((start, end))
    #             start = end
    #         end += 1

    #     max_s, max_e = 0, 1

    #     for start, end in a:
    #         while start > 0 and end < n and s[start-1]== s[end]:
    #             start, end = start-1, end+1

    #         if end - start > max_e - max_s:
    #             max_s, max_e = start, end


    #     return s[max_s:max_e]


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # dp[i][j]: s[i:j+1] 是否是回文串
        start, max_len = 0, 1
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and length > max_len:
                    max_len = length
                    start = i

        return s[start:start+max_len]



        
# @lc code=end

