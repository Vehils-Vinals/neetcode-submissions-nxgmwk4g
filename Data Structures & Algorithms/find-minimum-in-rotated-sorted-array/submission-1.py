class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mini = float('inf')
        while l < r:
            k = (l+r) // 2
            mini = min(mini, nums[k])
            if nums[k] > nums[r]:
                l = k + 1
            else:
                r =  k - 1
        return min(mini, nums[l])
