class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s, letter_t = [0]*26, [0]*26
        for elt in s:
            letter_s[ord(elt) - ord('a')] += 1
        for elt in t:
            letter_t[ord(elt) - ord('a')] += 1
        return letter_s == letter_t