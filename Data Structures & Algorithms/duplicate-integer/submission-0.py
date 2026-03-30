class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for elt in nums:
            if elt in duplicates:
                return True
            duplicates.add(elt) 
        return False