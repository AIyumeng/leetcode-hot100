#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        match = [False]*(n+1)
        match[0] = True

        for i in range(1,n+1):
            for word in wordDict:
                w_l = len(word)
                if i>=w_l and match[i-w_l] and s[i-w_l:i]==word:
                    match[i] = True
                    break

        return match[-1]

        
# @lc code=end

