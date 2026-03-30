class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        Leftmax, Rightmax = height[l], height[r]
        res = 0
        while l < r:
            if Leftmax < Rightmax:
                l += 1
                Leftmax = max(height[l], Leftmax)
                res += Leftmax - height[l]
            else:
                r -= 1
                Rightmax = max(height[r], Rightmax)
                res += Rightmax - height[r]
        return res
        

            
