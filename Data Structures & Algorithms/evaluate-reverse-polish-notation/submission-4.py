class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x + y)
            elif val == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x * y)
            elif val == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif val == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(val))
            
        return stack[-1]