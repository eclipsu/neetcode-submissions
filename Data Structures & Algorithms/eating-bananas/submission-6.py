import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_is_valid(k):
            hour = 0

            for pile in piles:
                hour += math.ceil(pile / k)
            
            return hour <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if k_is_valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left