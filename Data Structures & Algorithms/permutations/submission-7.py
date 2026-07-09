class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1: return [nums[:]]

        for i in range(len(nums)):
            num = nums.pop(0)

            prems = self.permute(nums)

            for prem in prems:
                prem.append(num)
            
            result.extend(prems)
            nums.append(num)
        
        return result
            

