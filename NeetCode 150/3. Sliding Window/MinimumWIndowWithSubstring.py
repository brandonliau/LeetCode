class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans, smap, tmap = "", {}, {}
        left, minw = 0, float('inf')

        if len(s) < len(t):
            return ans

        for item in t:
            tmap[item] = tmap.get(item, 0) + 1

        have, need = 0, len(tmap)
        
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1

            if s[i] in tmap and smap[s[i]] == tmap[s[i]]:
                have += 1
            
            while have == need:
                if i - left < minw:
                    minw = i - left
                    ans = s[left : i + 1]
                smap[s[left]] -= 1

                if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                    have -= 1
                left += 1

        return ans