#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode()
        cur = dummy
        while list1 or list2:
            val1 = list1.val if list1 else 200
            val2 = list2.val if list2 else 200
            if val1<val2:
                cur.next = list1 # not ListNode(val1)
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        return dummy.next
# @lc code=end

