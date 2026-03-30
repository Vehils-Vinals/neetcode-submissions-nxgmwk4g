class Solution:
    def isValid(self, s: str) -> bool:
        closed = {")": "(", "]": "[", "}": "{"}

        stack = []
        for elt in s:

            if elt not in closed.keys():
                stack.append(elt)
                continue
            if len(stack)==0:
                return False
            if stack[-1] == closed[elt]:
                stack.pop()
            else:
                return False

        return len(stack)==0
                
