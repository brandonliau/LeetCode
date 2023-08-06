class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, left, temp = 0, 0, set()

        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[i])
            ans = max(ans, len(temp))
        return ans
