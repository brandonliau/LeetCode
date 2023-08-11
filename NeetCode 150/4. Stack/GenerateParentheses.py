class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, ans = [], []

        def recursive(open, closed):
            if open == closed == n:
                ans.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                recursive(open + 1, closed)
                stack.pop()
            
            if closed < open:
                stack.append(')')
                recursive(open, closed + 1)
                stack.pop()
    
        recursive(0,0)
        return ans