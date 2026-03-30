class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, elt in enumerate(temperatures):
            while stack and elt>stack[-1][0]:
                t, ind = stack.pop()
                ans[ind] = i - ind
            stack.append((elt, i))
        return ans