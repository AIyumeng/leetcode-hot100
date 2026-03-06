#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:

    #     def dfs(i, path):
    #         if i == n:
    #             results.append(path)
    #             return

    #         for xx in a[digits[i]]:
    #             dfs(i+1, path + xx)
    #     a = {
    #         "2": ["a", "b", "c"],
    #         "3": ["d", "e", "f"],
    #         "4": ["g", "h", "i"],
    #         "5": ["j", "k", "l"],
    #         "6": ["m", "n", "o"],
    #         "7": ["p", "q", "r", "s"],
    #         "8": ["t", "u", "v"],
    #         "9": ["w", "x", "y", "z"],
    #     }
    #     if not digits:
    #         return []
    #     results = []
    #     n = len(digits)
    #     dfs(0, "")
    #     return results
    

    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
        
    #     # 数字-字母映射表
    #     num2char = {
    #         "2": ["a", "b", "c"],
    #         "3": ["d", "e", "f"],
    #         "4": ["g", "h", "i"],
    #         "5": ["j", "k", "l"],
    #         "6": ["m", "n", "o"],
    #         "7": ["p", "q", "r", "s"],
    #         "8": ["t", "u", "v"],
    #         "9": ["w", "x", "y", "z"],
    #     }
        
    #     results = []
    #     n = len(digits)
        
    #     def dfs(i, path):
    #         if i == n:
    #             # 将列表路径转为字符串，加入结果
    #             results.append("".join(path))
    #             return
            
    #         # 遍历当前数字的所有字母
    #         for char in num2char[digits[i]]:
    #             # 1. 做出选择：将当前字母加入路径
    #             path.append(char)
    #             # 2. 递归下探：处理下一个数字
    #             dfs(i+1, path)
    #             # 3. 回溯：撤销选择（手动pop，显式回溯）
    #             path.pop()
        
    #     # 初始调用：从第0个数字开始，路径为空列表
    #     dfs(0, [])
    #     return results

    def letterCombinations(self, digits: str) -> List[str]:
        a = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []

        results = a[digits[0]]
        i = 1
        n = len(digits)
        while i < n:
            new_results = []
            for rr in results:
                for xx in a[digits[i]]:
                    new_results.append(rr + xx)
            results = new_results
            i += 1

        return results


# @lc code=end
