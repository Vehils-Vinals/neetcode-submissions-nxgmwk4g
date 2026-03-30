class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        Left_max, Right_max = height[l], height[r]
        area = 0
        while l < r:
            if Left_max < Right_max:
                l += 1
                area += max(min(Left_max, Right_max) - height[l], 0)
            else:
                r -= 1
                area += max(min(Left_max, Right_max) - height[r], 0)
            Left_max = max(Left_max, height[l])
            Right_max = max(Right_max, height[r])

        return area

            

