class Solution:
    def is_alpha_numeric(self, s):
        return (
            (0 <= (ord(s) - ord("a")) < 26) or
            (0 <= (ord(s) - ord("0")) < 9)
        )
    def isPalindrome(self, c) :
        c = c.lower()       
        l, r = 0, len(c)-1
        while l<=r and l < len(c) and r > -1 :
            while l < len(c) - 1 and not self.is_alpha_numeric(c[l]):
                l += 1
            while r > 0 and not self.is_alpha_numeric(c[r]):
                r -= 1
            if (self.is_alpha_numeric(c[r]) and
            self.is_alpha_numeric(c[l]) and
              c[l] != c[r]):
                return False
            l += 1
            r -= 1
        return True