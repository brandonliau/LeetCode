class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset, maxlength = set(nums), 0

        for n in nums:
            if n - 1 not in numset:
                length = 1
                while n + length in numset:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength