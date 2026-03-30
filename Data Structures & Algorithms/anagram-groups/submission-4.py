class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for elt in strs:
            c = [0]*26
            for s in elt:
                c[ord(s) - ord('a')] += 1
            dic[tuple(c)].append(elt)
        return list(dic.values())
