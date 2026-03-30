class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        if target > nums[-1] and target < nums[0]:
            return -1
        while l <= r :
            k = (l+r)//2
            if target == nums[k]:
                return k

            elif target <= nums[-1]:
                if nums[k] <= nums[-1]:
                    if nums[k] < target:
                        l = k + 1
                    else: 
                        r = k - 1
                else:
                    l = k + 1
                
            elif target >= nums[0]:
                if nums[k] >= nums[0]:
                    if nums[k] < target:
                        l += 1
                    else:
                        r = k - 1
                else:
                    r = k - 1
        return -1
