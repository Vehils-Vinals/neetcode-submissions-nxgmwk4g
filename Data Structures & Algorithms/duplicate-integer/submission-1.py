class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = set()
        for elt in nums:
            if elt in already_seen:
                return True
            already_seen.add(elt)
        return False