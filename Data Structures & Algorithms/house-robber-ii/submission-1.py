class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        rob1, rob2 = 0, 0

        for n in nums[:-1]:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp
        
        res = rob2

        rob1, rob2 = 0, 0

        for n in nums[1:]:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp
        
        res = max(res,rob2)

        return res