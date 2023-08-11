class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        ans = slow = 0
        
        for p, s in pair:
            time = (target - p) / s
            if time > slow:
                ans += 1
                slow = time
                
        return ans
