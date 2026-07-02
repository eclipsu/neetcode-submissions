class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in cache:
                size = 0
                while (num + size) in cache:
                    size += 1
                longest = max(longest, size)
        return longest
