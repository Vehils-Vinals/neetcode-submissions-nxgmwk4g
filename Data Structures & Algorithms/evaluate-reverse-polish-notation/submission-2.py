class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []

        for elt in tokens:
            if elt == '+':
                stack.append(stack.pop() +
                            stack.pop())
            elif elt == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif elt == '*':
                stack.append(stack.pop()*stack.pop())
            elif elt == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b/a)))
            else:
                stack.append(int(elt))
        return stack[0]

        

