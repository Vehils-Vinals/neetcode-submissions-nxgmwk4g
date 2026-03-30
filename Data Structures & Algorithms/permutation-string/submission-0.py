class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        for elt in s1:
            count_s1[elt] = count_s1.get(elt, 0) + 1
        
        count_s2 = {}
        l = 0
        for r in range(len(s2)):
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
            while r - l + 1 > len(s1):
                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]
                l += 1
            print(count_s2)
            if count_s2 == count_s1:
                return True
        return False