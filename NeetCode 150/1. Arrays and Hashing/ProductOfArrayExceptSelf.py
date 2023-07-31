class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, post = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        return ans