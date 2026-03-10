#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []
        
#         # 递归函数：level表示当前层数（从0开始）
#         def dfs(node, level):
#             if not node:
#                 return
#             # 若当前层数超出结果列表长度，新增一层
#             if level >= len(res):
#                 res.append([])
#             # 将当前节点值加入对应层的列表
#             res[level].append(node.val)
#             # 递归处理左、右子树（层数+1）
#             dfs(node.left, level + 1)
#             dfs(node.right, level + 1)
        
#         dfs(root, 0)
#         return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 空树直接返回空列表
        if not root:
            return []
        
        # 初始化队列和结果列表
        from collections import deque
        queue = deque([root])
        res = []
        
        # 逐层处理队列中的节点
        while queue:
            # 当前层的节点数量（关键：确保只处理当前层）
            level_size = len(queue)
            # 存储当前层的节点值
            level_res = []
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                # 弹出队首节点
                node = queue.popleft()
                # 记录当前节点值
                level_res.append(node.val)
                
                # 左子节点非空则加入队列
                if node.left:
                    queue.append(node.left)
                # 右子节点非空则加入队列
                if node.right:
                    queue.append(node.right)
            
            # 将当前层结果加入总结果
            res.append(level_res)
        
        return res



# @lc code=end

