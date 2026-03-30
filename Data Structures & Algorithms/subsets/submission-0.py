class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        ans = []
        for i in range(len(nums)+1):
            tmp = combinations(nums, i)
            for elt in tmp:
                ans.append(list(elt))
        return ans