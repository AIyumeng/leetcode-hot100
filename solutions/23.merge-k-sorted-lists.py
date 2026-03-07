#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            dummy = ListNode()
            cur = dummy
            while lists[0] or lists[1]:
                val1 = lists[0].val if lists[0] else 20000
                val2 = lists[1].val if lists[1] else 20000
                if val1<val2:
                    cur.next = lists[0]
                    cur = cur.next
                    lists[0] = lists[0].next
                else:
                    cur.next = lists[1]
                    cur = cur.next
                    lists[1] = lists[1].next
            return dummy.next
        else:

            return self.mergeKLists([self.mergeKLists(lists[:n//2]),self.mergeKLists(lists[n//2:])])
            
        
# @lc code=end

