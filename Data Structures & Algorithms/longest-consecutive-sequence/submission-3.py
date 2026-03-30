from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            if not dic[num]:
                dic[num] = dic[num-1] + dic[num+1] + 1
                dic[num - dic[num-1]] = dic[num]
                dic[num + dic[num+1]] = dic[num]
        
        maxi = 0
        for v in dic.values(): 
            maxi = max(v, maxi)
        return maxi