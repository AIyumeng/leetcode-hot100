#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                
                # 记录左上
                temp = matrix[i][j]
                
                # 左下 → 左上
                matrix[i][j] = matrix[n - 1 - j][i]
                
                # 右下 → 左下
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                
                # 右上 → 右下
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                
                # 左上 → 右上
                matrix[j][n - 1 - i] = temp

                
# @lc code=end

