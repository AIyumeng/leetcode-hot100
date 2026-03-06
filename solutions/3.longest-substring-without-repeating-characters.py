#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import collections
        max_len = 0
        cur = collections.deque()

        for i, ss in enumerate(s):
            if ss in cur:
                while cur[0] != ss:
                    cur.popleft()
                cur.popleft()

            cur.append(ss)
            max_len = max(max_len, len(cur))

        return max_len

        # left = 0
        # max_len = 0
        # char_index = {}
        # for right in range(len(s)):
        #     if s[right] in char_index and char_index[s[right]] >= left:
        #         left = char_index[s[right]] + 1
            
        #     char_index[s[right]] = right
        #     max_len = max(max_len, right - left+1)

        # return max_len


# @lc code=end
