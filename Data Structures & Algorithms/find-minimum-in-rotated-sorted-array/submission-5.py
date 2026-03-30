class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        mini = float('inf')

        while l < r:
            m = (l+r)//2
            mini = min(mini, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return min(mini, nums[l])

