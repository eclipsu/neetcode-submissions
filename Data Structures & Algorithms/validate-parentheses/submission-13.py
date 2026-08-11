class Solution:
    def isValid(self, s: str) -> bool:

        bracket = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []

        for char in s:
            if char in bracket:
                if not stack or stack[-1] != bracket[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
                

        return not stack
