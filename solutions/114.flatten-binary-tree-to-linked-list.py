#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        deque = [root]
        dummy = TreeNode()
        while deque:
            cur = deque.pop()
            dummy.right = cur
            dummy.left = None
            if cur.right is not None:
                deque.append(cur.right) 
            if cur.left is not None:
                deque.append(cur.left) 

            dummy = dummy.right


                

    

        
# @lc code=end

