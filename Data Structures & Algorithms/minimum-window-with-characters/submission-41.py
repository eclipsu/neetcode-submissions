class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""

        setW = {}
        setT = {}

        for char in t:
            setT[char] = 1 + setT.get(char, 0)
        
        have = 0
        need = len(setT)

        result = {
            "range" : [-1, -1],
            "size" : float("infinity")
        }

        left = 0
        for right in range(len(s)):
            char = s[right]
            setW[char] = 1 + setW.get(char, 0)

            if char in setT and setW[char] == setT[char]:
                have += 1
            
            while have == need:
                size = (right - left) + 1
                if size <= result["size"]:
                    result["range"] = [left, right]
                    result["size"] = size
                
                left_char = s[left]
                setW[left_char] -= 1
                if left_char in setT and setW[left_char] < setT[left_char]:
                    have -= 1

                left += 1
        
        l, r = result["range"]
        return s[l : r + 1] if result["size"] != float("infinity") else ""

