class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        previous_operator = "+"
        s += "@"
        for i, c in enumerate(s):
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == "(":
                stack.append(previous_operator)
                previous_operator = "+"
            else:
                if previous_operator == "*":
                    stack.append(stack.pop() * cur)
                elif previous_operator == "/":
                    stack.append(int(stack.pop() / cur))
                elif previous_operator == "+":
                    stack.append(cur)
                elif previous_operator == "-":
                    stack.append(-cur)
                cur = 0
                previous_operator = c
                if c == ")":
                    while isinstance(stack[-1], int):
                        cur += stack.pop()
                    previous_operator = stack.pop()

        return sum(stack)
