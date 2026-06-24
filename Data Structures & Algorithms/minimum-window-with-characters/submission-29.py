class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, countW = {}, {}

        result = {
            "range": [-1, -1],
            "size": float("infinity")
        }

        for c in t: 
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        left = 0
        for right in range(len(s)):
            c = s[right]
            countW[c] = 1 + countW.get(c, 0)

            if c in countT and countW[c] == countT[c]:
                have += 1
            
            while have == need:
                size = (right - left) + 1

                if size <= result["size"]:
                    result["range"] = [left, right] 
                    result["size"] = size
                
                C = s[left]
                countW[C] -= 1
                if C in countT and countW[C] < countT[C]:
                    have -= 1
                
                left += 1

        l, r = result["range"]
        return s[l:r + 1] if result["size"] != float("infinity") else ""