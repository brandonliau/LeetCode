class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for item in nums:
            if item in numset:
                return True
            numset.add(item)
            
        return False
    