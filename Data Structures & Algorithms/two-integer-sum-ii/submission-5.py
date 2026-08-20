class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1
        while l < h:
            total = numbers[l] + numbers[h]
            if total > target:
                h -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, h + 1]
        