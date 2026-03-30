class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}
        for elt in nums:
            count[elt] = count.get(elt, 0) + 1
        for key, value in count.items():
            freq[value].append(key)
        del count
        ans = []
        i = 1
        while len(ans) < k:
            ans += freq[-i]
            i += 1
        return ans