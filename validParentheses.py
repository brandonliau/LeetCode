class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif i == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif i == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return len(stack) == 0
        
class OptimalSolution:
    def isValid(self, s: str) -> bool:
        map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in map:
                stack.append(i)
            elif stack and map[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return len(stack) == 0
