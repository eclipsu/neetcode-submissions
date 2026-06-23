from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]

        for number, frequency in count.items():
            bucket[frequency].append(number)
        
        result = []

        for i in range(len(nums), 0, -1):
            for number in bucket[i]:
                result.append(number)
            
                if len(result) == k:
                    return result

        print(result)
        
