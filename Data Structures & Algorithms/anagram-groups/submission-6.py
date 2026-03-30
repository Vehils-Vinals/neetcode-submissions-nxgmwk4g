from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        code_str = defaultdict(list)

        for str in strs:
            list_str = [0]*26
            for s in str:
                list_str[ord(s) - ord("a")] += 1
            code_str[tuple(list_str)].append(str)
        
        res = []
        for val in code_str.values():
            res.append(val)
        return res


