class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        seen = nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                seen = min(seen, nums[left])
                break

            mid = (left + right) // 2
            seen = min(nums[mid], seen)

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return seen
