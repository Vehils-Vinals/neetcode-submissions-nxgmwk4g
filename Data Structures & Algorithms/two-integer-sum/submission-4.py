class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, elt in enumerate(nums):
            diff = target - elt
            print(diff, dic)
            if diff in dic:
                return [dic[diff], i]
            dic[elt] = i
        return []
