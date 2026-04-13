class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pair = {
            "(":")",
            "{": "}",
            "[": "]"
        }

        for p in s:
            if p in "[({":
                seen.append(p)
            else:
                if not seen or pair[seen[-1]] != p:
                    return False
                seen.pop()

        return True if len(seen) == 0 else False

       
