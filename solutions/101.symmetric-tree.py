#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isSame(a,b):
            if a ==None and b==None:
                return True
            elif a ==None and b!=None:
                return False
            elif a !=None and b==None:
                return False
            else:
                if a.val!=b.val:
                    return False
                return isSame(a.left, b.right) and isSame(a.right,b.left)
            


        return isSame(root.left, root.right)
    
        

        
# @lc code=end

