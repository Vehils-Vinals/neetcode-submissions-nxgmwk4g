class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        max_l = 0
        set_sub = {}

        l, r = 0, 0
        while r < len(s):
            print(set_sub)
            if s[r] in set_sub:
                max_l = max(max_l, r-l)
                l = max(l, set_sub[s[r]] + 1)
            set_sub[s[r]] = r
            
            r += 1

        return max(max_l, r-l)
    

        