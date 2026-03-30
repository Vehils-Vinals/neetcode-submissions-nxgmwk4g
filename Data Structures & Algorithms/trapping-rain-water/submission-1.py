class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0
        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]

        while l<r:
            if height[l]<height[r]:
                l += 1
                maxleft = max(maxleft, height[l])
                total += maxleft-height[l]
            else:
                r -= 1
                maxright = max(maxright, height[r])
                total += maxright-height[r]
        return total
