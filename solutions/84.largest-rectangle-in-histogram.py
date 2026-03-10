#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
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

        


        # if not heights:
        #     return 0
        # if len(heights) == 1:
        #     return heights[0]

        # min_x = min(heights)
        # min_i = heights.index(min_x)

        # return max(
        #     min_x*len(heights), 
        #     self.largestRectangleArea(heights[:min_i]),
        #     self.largestRectangleArea(heights[min_i+1:])
            
        #     )
        
# @lc code=end

