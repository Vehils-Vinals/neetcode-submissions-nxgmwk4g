class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for elt in set_nums:
            if elt - 1 not in set_nums:
                l = 1
                while elt + l in set_nums:
                    l += 1
                longest = max(l, longest)
        return longest
            