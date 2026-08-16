class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        counter = collections.Counter(nums)

        for num, freq in counter.items():
            buckets[freq].append(num)
        

        result = []
        for bucket in range(len(nums), 0, -1):
            for element in buckets[bucket]:
                result.append(element)
            if len(result) == k:
                return result
