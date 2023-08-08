class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length, s1map, s2map, left = len(s1), {}, {}, 0
        
        for item in s1:
            s1map[item] = s1map.get(item, 0) + 1

        for i in range(len(s2)):
            s2map[s2[i]] = s2map.get(s2[i], 0) + 1
            if i - left >= length:
                s2map[s2[left]] -= 1
                if s2map[s2[left]] == 0: 
                    del s2map[s2[left]]
                left += 1
            if s1map == s2map:
                return True
            
        return False