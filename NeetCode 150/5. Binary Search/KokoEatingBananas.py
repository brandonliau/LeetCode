class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high, ans = 1, max(piles), float('inf')

        while low <= high:
            rate = (low + high) // 2
            count = 0
            for item in piles:
                count += math.ceil(item / rate)
            
            if count <= h:
                ans = min(ans, rate)
                high = rate - 1
            else:
                low = rate + 1

        return ans