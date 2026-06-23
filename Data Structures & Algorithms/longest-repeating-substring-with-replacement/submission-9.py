class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # "XX[YYYB]", if k = 1

        # how are we going to figure out if it can be replaced
        # note that we can replace it by ANYTHING, so we might as well figure out, what is the max 

        bucket = [0] * 26 
        left = 0          
        longest = 0 

        for right in range(len(s)):
            bucket[ord(s[right]) - 65] += 1

            while (right - left + 1) - max(bucket) > k:
                bucket[ord(s[left]) - 65] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest