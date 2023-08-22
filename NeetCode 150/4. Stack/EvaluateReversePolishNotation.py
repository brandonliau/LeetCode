class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(item))
        return stack[0]