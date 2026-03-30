class Solution:
    def isValid(self, s: str) -> bool:
        opened = {'(':')', '[':']', '{':'}'}
        closed = {')':'(', ']':'[', '}':'{'}

        stack = []

        for elt in s:
            if elt in opened:
                stack.append(elt)
            else:
                if len(stack)==0:
                    return False
                elif closed[elt] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
