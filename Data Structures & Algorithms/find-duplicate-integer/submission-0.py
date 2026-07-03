class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: break
        
        turtle = nums[0]
        while turtle != slow:
            turtle = nums[turtle]
            slow = nums[slow]
        
        return slow