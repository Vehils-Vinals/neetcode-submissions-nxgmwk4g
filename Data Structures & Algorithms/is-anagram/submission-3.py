class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        elt_s, elt_t = {}, {}
        for dic, li in zip([elt_s, elt_t], [s, t]):
            for elt in li:
                dic[elt] = dic.get(elt, 0) + 1
        
        return elt_s == elt_t
