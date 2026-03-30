class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first_go = [1]
        for i in range(1, len(nums)):
            first_go.append(first_go[i-1] * nums[i-1])
        
        second_go = [1]
        for i in range(len(nums)-1, -1, -1):
            second_go.append(second_go[len(nums) - i - 1] * nums[i])

        res = []
        for i in range(len(first_go)):
            res.append(first_go[i] * second_go[len(nums) - i - 1])
        return res




