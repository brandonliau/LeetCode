class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for item in strs:
            chars = [0] * 26
            for char in item:
                chars[ord(char) - ord('a')] += 1
            ans[tuple(chars)].append(item)
        return ans.values()
