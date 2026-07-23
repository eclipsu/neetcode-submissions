class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kWorks(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            return hours <= h
        
        left = 1 
        right = max(piles)
        while left < right:
            mid = (right + left) // 2

            if kWorks(mid):
                right = mid
            else:
                left = mid + 1
            
        return left