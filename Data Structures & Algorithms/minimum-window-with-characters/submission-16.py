class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, count_w = {}, {}

        left = 0
        result = [[-1, -1], float("infinity")]

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        have, need = 0, len(count_t)

        for right in range(len(s)):
            count_w[s[right]] = 1 + count_w.get(s[right], 0)

            if s[right] in count_t and count_w[s[right]] == count_t[s[right]]:
                have += 1

            while have == need:
                size = right - left + 1

                if size < result[1]:
                    result[0] = [left, right]
                    result[1] = size

                count_w[s[left]] += -1

                if s[left] in count_t and count_w[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        l, r = result[0]
        return s[l:r + 1] if result[1] != float("infinity") else ""