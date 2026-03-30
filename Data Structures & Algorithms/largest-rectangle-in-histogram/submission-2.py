class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        tmp = 0
        for i, elt in enumerate(heights):
            boolean = False
            print(stack)
            while stack and elt < stack[-1][1]:
                boolean = True
                res = max((i-stack[-1][0])*stack[-1][1], res)
                tmp = stack[-1][0]
                stack.pop()
            if boolean:
                stack.append([tmp, elt])
            else:
                stack.append([i, elt])
            res = max(res, elt)

        while stack:
            print(stack)

            res = max(res, (len(heights) - stack[-1][0])*stack[-1][1])
            stack.pop()
        return res


