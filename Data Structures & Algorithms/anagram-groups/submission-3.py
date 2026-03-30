class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for elt in strs:
            count = [0]*26
            for s in elt:
                count[ord(s)-ord('a')] += 1
            dic[tuple(count)].append(elt)
        return dic.values()

