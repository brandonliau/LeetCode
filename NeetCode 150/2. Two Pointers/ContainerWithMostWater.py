class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans, left, right = 0, 0, len(height) - 1

        while True:
            volume = (right - left) * min(height[left], height[right])
            if volume > ans:
                ans = volume
            if right == left + 1:
                break
            if height[right] > height[left]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
        
        return ans
    