class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxa, stack = 0, []
        for i, v in enumerate(heights):
            mini = i
            while stack and stack[-1][1] > v:
                index, height = stack.pop()
                maxa = max(maxa, height * (i - index))
                mini = index
            stack.append((mini, v))

        for i, v in stack:
            maxa = max(maxa, v * (len(heights) - i))

        return maxa