class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        result = []

        for permutation in permutations:
            for i in range(len(permutation) + 1):
                prem = permutation.copy()
                prem.insert(i, nums[0])
                result.append(prem)
        
        return result


