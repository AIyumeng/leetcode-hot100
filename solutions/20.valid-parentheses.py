#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        a = []
        b = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ss in s:
            if ss not in b:
                a.append(ss)
            else:
                if not a:
                    return False
                elif a[-1]!=b[ss]:
                    return False
                else:
                    a.pop()
                
        return not a
        
# @lc code=end

