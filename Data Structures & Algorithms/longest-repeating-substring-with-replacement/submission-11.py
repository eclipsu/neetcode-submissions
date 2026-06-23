class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        bucket = [0] * 26 
        left = 0

        for right in range(len(s)):
            bucket[ord(s[right]) - ord('A')] += 1

            while (right - left + 1 )  - max(bucket) > k:
                bucket[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            longest = max(longest, (right - left + 1 ))
        
        return longest
