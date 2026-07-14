class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow: break
        
        turtle = 0
        while True:
            slow = nums[slow]
            turtle = nums[turtle]
            if turtle == slow: return turtle
        
