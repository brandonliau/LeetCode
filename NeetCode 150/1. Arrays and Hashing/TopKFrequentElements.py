class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction, bucket, ans = {}, [[] for i in range(len(nums) + 1)], []
        for item in nums:
            diction[item] = diction.get(item, 0) + 1
        for key, v in diction.items():
            bucket[v].append(key)
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans