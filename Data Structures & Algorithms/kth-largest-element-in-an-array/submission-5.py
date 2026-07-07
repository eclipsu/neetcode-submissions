class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        return sorted(nums)[len(nums) - k]