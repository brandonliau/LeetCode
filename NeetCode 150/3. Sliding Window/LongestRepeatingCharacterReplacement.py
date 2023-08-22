class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, left, maxfreq, count = 0, 0, 0, {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            maxfreq = max(maxfreq, count[s[i]])
            while (i - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)

        return ans
    