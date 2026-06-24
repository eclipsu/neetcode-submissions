class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]: return mid

            # we are in lft portion
            if nums[mid] >= nums[left]:
                # if target is less than mid or target is more than left, we move to right
                # 1l, 3, 5m, 0, 1r 
                # t = 0, target < mid yes, target > 1 yes
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                 
            # we are in rgt portion
            else:
                # if target is more than mid or target is less than right, we move to left
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else: 
                    left = left + 1
        return -1 