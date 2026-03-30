class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, elt in enumerate(nums):
            if elt in seen:
                return [seen[elt], i]
            seen[target - elt] = i
        return
