class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # "XX[YYYB]", if k = 1

        # how are we going to figure out if it can be replaced
        # note that we can replace it by ANYTHING, so we might as well figure out, what is the max 

        bucket = [0] * 26 # 0 -> a, 1 -> b, if bucket[0] = 3, there are 3 A's
        left = 0          # "[" <--- 
        longest = 0 

        for right in range(len(s)):
            bucket[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(bucket) > k:
                bucket[ord(s[left]) - ord('A')] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest