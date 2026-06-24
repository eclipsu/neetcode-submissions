class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = float("infinity")

        # [4,5,[0],1,2,3]
        # [l4m,5r,0,1,2,3]
        while left < right:
            # edge case - if the array is already sorted:
            if nums[left] < nums[right]: return nums[left]
            
            mid = left + (right - left) // 2
            minimum = min(minimum, nums[mid])

            # [3,4,5,6l,1m,2r] -> 1 is minimum 1 > 6, 
            # [3,4,5,6,1,2r] -> 1 is minimum 1 < 6 so r = m - 1, 
            # [l..3,4,5m,..6,1,2r] -> 5 is minimum 5 > 3 so we don't have to check l-m, so l = m + 1

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                    
        return nums[left]



