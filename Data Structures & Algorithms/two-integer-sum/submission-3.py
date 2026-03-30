class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            if target-value in seen:
                return [seen[target-value], i]
            seen.update({value: i})
        return 'No pair of element are adding up to the target'