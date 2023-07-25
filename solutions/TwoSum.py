class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numDict = {}
        for i in range(len(nums)):
            if target - nums[i] in numDict:
                return [i, numDict[target - nums[i]]]
            else:
                numDict[nums[i]] = i
