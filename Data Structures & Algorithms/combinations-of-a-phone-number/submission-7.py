class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        combinations = []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(current, index):
            if len(digits) == index:
                combinations.append(current)
                return 
            
            for letter in phone[digits[index]]:
                dfs(current + letter, index + 1)
            return
            
        dfs("", 0)
        return combinations