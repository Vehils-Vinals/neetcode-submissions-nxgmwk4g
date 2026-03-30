class Solution:
    def alpha_num(self, c):
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            return True
        elif ord(c) >= ord('A') and ord(c) <= ord('Z') >= 0:
            return True
        elif ord(c) >= ord('0') and ord(c) <= ord('9') >= 0:
            return True
        
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            print(1)
            while l < r and not self.alpha_num(s[l]):
                l += 1
            while l <r and not self.alpha_num(s[r]):
                r -= 1
            print(s[r].lower(), s[l].lower())
            if s[r].lower() != s[l].lower():
                return False
            l += 1
            r -= 1
        return True