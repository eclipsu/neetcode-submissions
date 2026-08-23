class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        bucket_s = [0] * 26
        bucket_t = [0] * 26

        for c in s:
            bucket_s[ord('a') - ord(c)] += 1

        for c in t:
            bucket_t[ord('a') - ord(c)] += 1
        
        return bucket_t == bucket_s
