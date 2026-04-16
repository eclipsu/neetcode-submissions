class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        best = nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                best = nums[left]
                break

            mid = (left + right) // 2
            best = nums[mid]

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
            
        return best
