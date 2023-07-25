class Solution:
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
