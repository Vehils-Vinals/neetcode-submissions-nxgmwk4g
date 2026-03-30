class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maxi = max(area, maxi)

            if heights[r] > heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[r-1] > heights[l+1]:
                l += 1
            else:
                r -= 1
        return maxi
