from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r= 1, max(piles)
        res = r
        def time_eating(piles, k):
            hours = 0
            for elt in piles:
                hours += ceil(elt/k)
            return hours
        
        while l <= r:
            k = (l+r) // 2
            if time_eating(piles, k) <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
                
