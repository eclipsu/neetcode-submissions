class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        ss_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        l = 0
        r = len(s1) - 1
    
        while r < len(s2):
            ss_count = [0] * 26 
            for i in range(l, r + 1):
                ss_count[ord(s2[i]) - ord('a')] += 1
            
            
            if ss_count == s1_count:
                return True

            l += 1
            r += 1
        return False


        