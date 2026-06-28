class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in nums:
                size = 0
                while (num + size) in nums:
                    size += 1
                longest = max(longest, size)
        return longest
