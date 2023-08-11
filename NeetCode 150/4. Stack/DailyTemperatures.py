class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures) 
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                ans[x] = i - x

            stack.append(i)
        return ans