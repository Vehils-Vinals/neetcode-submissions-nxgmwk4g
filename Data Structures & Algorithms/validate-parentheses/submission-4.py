class Solution:
    def isValid(self, s: str) -> bool:
        closed = {')':'(', ']':'[', '}':'{'}

        stack = []

        for elt in s:
            if not elt in closed:
                stack.append(elt)
                continue
            if not stack or closed[elt] != stack[-1]:
                return False
            stack.pop()
        return not stack
