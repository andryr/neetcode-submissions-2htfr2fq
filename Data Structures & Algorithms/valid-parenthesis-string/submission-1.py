class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_1 = []
        stack_2 = []
        for i, c in enumerate(s):
            if c == "(":
                stack_1.append(i)
            elif c == "*":
                stack_2.append(i)
            else:
                if stack_1:
                    stack_1.pop()
                elif stack_2:
                    stack_2.pop()
                else:
                    return False
        while stack_1 and stack_2:
            i, j = stack_1.pop(), stack_2.pop()
            if j < i:
                return False
        return not stack_1
                