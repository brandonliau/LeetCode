class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans, length = [], len(nums)
        nums.sort()
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            point, left, right = i, i + 1, length - 1
            while left < right:
                sum = nums[point] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans.append([nums[point], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return ans
    