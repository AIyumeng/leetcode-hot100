#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        # 在末尾补一个0，强制清空栈
        heights.append(0)
        
        for i in range(len(heights)):
            # 当前高度小于栈顶高度时，计算面积
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                # 如果栈为空，说明左边没有更小的
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        return max_area



    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]
        max_area = 0

        for i in range(m):
            for j in range(n):
                if i==0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = int(matrix[i][j]) + dp[i-1][j] if matrix[i][j] == '1' else 0

        for i in range(m):
            area = self.largestRectangleArea(list(map(int,dp[i])))
            max_area = max(max_area, area)

        return max_area

        
# @lc code=end

