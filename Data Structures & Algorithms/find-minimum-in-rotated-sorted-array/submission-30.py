class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:

            if nums[right] > nums[left]: return nums[left]
            
            mid = (right + left) // 2
            # left sorted array
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

            # right sorted array


