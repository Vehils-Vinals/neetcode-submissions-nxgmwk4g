class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_val = set(nums)
        max_lenght = 0
        for elt in all_val:
            if elt-1 not in all_val:
                lenght = 1
                while lenght + elt in all_val:
                    lenght += 1
                max_lenght = max(lenght, max_lenght)
        return max_lenght