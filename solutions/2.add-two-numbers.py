#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        c = 0 # 进位
        while l1 or l2 or c:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            d = a + b + c # 和
            c = d // 10
            e = d % 10 
            cur.next = ListNode(e)
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next

# @lc code=end

