class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for k in tokens:
            if k == "*":
                stack.append(stack.pop()*stack.pop())

            elif k == "+":
                stack.append(stack.pop()+stack.pop())
            elif k == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/float(a)))
            elif k == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            else:
                stack.append(int(k))
        return stack[0]
        