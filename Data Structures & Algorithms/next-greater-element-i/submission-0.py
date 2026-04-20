class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # we are going make "memory" to remember where the nums1's element's indices are

        index = {value: index for index, value in enumerate(nums1)   }
        
        # default is -1 if not found
        result = [-1] * len(nums1)
        stack = [] # monotonic decreasing stack that keeps track of lowest seen value so far

        for num in nums2:
            while stack and num > stack[-1]:
                last = stack.pop()
                idx = index[last]
                result[idx] = num
            if num in index:
                stack.append(num)
        return result
