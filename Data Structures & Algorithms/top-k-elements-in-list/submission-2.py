class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            for elt in nums:
                count[elt] = count.get(elt, 0) + 1
            freq = [[] for i in range(len(nums))]
            for key, value in count.items():
                freq[value-1].append(key)
            ans = []
            while len(ans) < k:
                ans += freq.pop()
            return ans

