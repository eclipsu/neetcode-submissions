import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def findK(k) -> bool:
            hour = 0    
            for pile in piles:
                hour += math.ceil(pile / k)
            return hour <= h
        
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if findK(mid):
                right = mid
            else:
                left = mid + 1
            
        return right
        
        