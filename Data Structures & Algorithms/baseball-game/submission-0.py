class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:

            if val == "+":
                p = stack.pop()
                s = p + stack[-1]
                stack.append(p)
                stack.append(s)
            elif val == "C":
                stack.pop()
            elif val == "D":
                stack.append(stack[-1]* 2)
            else:
                stack.append(int(val))
        
        res = sum([i for i in stack])
        return res