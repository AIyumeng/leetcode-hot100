#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter

        need = Counter(t)
        
        begin = 0
        end = 0
        valid = 0
        min_l = 100001
        min_string = ''
        cur = Counter()
        while end<len(s):
            c = s[end]
            end +=1
            if c in need:
                cur[c] = cur.get(c,0)+1
                if cur[c]==need[c]:
                    valid+=1

            while valid==len(need):
                if end-begin<min_l:
                    min_l=end-begin
                    min_string = s[begin:end]
                
                
                if s[begin] in need:
                    cur[s[begin]]-=1
                    if cur[s[begin]]<need[s[begin]]:
                        valid-=1
                begin+=1

            
        
        return min_string
        
# @lc code=end

