class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long = 0
        left = 0
        window = [0] * 26
        
        for right in range(len(s)):
            window[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(window) > k:
                window[ord(s[left]) - ord('A')] -= 1
                left += 1

            long = max(long, (right - left + 1))

        return long