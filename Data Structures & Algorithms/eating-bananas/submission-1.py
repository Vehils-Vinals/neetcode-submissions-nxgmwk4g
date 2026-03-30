import numpy as np

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        def timeEating(piles, k):
            somme = 0
            for i, elt in enumerate(piles):
                somme += np.ceil(elt/k)
            return somme
        
        mini = r
        while l<=r:
            k = (l+r)//2
            if timeEating(piles, k) <= h:
                mini = k
                r = k - 1
            if timeEating(piles, k) > h:
                l = k + 1
            
        return mini
            

            