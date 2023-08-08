class Solution:
    def trap(self, height: List[int]) -> int:
        ans, left, right = 0, 0, len(height) - 1
        maxleft, maxright = height[left], height[right]

        while left < right:
            if maxright >= maxleft:
                left += 1
                maxleft = max(maxleft, height[left])
                ans += maxleft - height[left]
            elif maxleft > maxright:
                right -= 1
                maxright = max(maxright, height[right])
                ans += maxright - height[right]
        
        return ans
    