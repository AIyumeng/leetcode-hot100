#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:

    #     res = []

    #     def dfs(s,i,j,n):
    #         if i==n and j==n:
    #             res.append(s)
    #         if i>n or i<j:
    #             return
         
    #         dfs(s+'(',i+1,j,n)
    #         dfs(s+')',i,j+1,n)

    #     dfs('',0,0,n)

    #     return res

            

            




    def generateParenthesis(self, n: int) -> List[str]:

        a = ['']
        for i in range(2*n):
            new_a = []
            for aa in a:
                left = aa + '('
                right = aa + ')'
                if left.count('(') <= n:
                    new_a.append(left)
                if right.count(')')<=right.count('('):
                    new_a.append(right)
            a = new_a
        return a
# @lc code=end

