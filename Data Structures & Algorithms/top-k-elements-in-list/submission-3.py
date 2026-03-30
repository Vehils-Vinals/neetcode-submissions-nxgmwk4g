from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freq_inv = defaultdict(list)
        for key, v in freq.items():
            freq_inv[v].append(key)
        res = []
        i = len(nums)
        while len(res) < k and i > -1:
            res.extend(freq_inv[i])
            i -= 1
        return res