class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, value in enumerate(nums):
            remain = target - nums[i]
            if remain in numDict:
                return [i, numDict[remain]]
            numDict[value] = i
            