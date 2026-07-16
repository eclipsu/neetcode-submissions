class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])
        result = []

        for permutation in permutations:
            for index in range(len(permutation) + 1):
                perms = permutation.copy()
                perms.insert(index, nums[0])
                result.append(perms)

        
        return result
        

        