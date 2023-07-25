class Solution:
    def makeMap(string):
            hash = {}
            for letter in string:
                if letter in hash:
                    hash[letter] += 1
                else:
                    hash[letter] = 1
            return hash
    
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Solution.makeMap(s)
        tmap = Solution.makeMap(t)
        return smap == tmap
