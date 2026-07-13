from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequency = [[] for _ in range(len(nums) + 1)]
        
        for num, count in count.items():
            frequency[count].append(num)
        
        result = []
        for i in range(len(nums), 0, -1):
            for num in frequency[i]:                  # unpack the bucket
                result.append(num)
                if len(result) == k:                  # stop once we have k elements
                    return result

        
        return result
