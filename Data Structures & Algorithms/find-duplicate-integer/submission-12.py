class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        turtle = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: break
        
        while True:
            slow = nums[slow]
            turtle = nums[turtle]
            if slow == turtle:
                return slow
        
