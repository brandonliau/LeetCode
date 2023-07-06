class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numDict = {}
        for i in range(len(nums)):
            if target - nums[i] in numDict:
                return [i, numDict[target - nums[i]]]
            else:
                numDict[nums[i]] = i

class OptimalSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numDict = {}
        for i, value in enumerate(nums): # enumerate adds indices to the nums list
            remainder = target - nums[i]
            if remainder in numDict:
                return [i, numDict[remainder]]
            else:
                numDict[value] = i
