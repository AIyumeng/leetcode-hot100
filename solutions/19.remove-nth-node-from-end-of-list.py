#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        l1 = l2 = dummy
        for _ in range(n):
            l1 = l1.next

        while l1.next:
            l1 = l1.next
            l2 = l2.next

        l2.next = l2.next.next
        return dummy.next
# @lc code=end

