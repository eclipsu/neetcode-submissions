class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graphs = {
            char: [] for word in words for char in word
        }

        for i in range(len(words) - 1):
            wordA, wordB = words[i], words[i + 1]
            minLen = min(len(wordA), len(wordB))

            if len(wordA) > len(wordB) and wordA[:minLen] == wordB[:minLen]:
                return ""

            for char in range(minLen):
                if wordA[char] != wordB[char]:
                    graphs[wordB[char]].append(wordA[char])
                    break

        gray = set()
        black = set()
        result = []

        def dfs(char):
            if char in gray:
                return True

            if char in black:
                return False

            gray.add(char)

            for neighbour in graphs[char]:
                if dfs(neighbour):
                    return True

            gray.remove(char)
            black.add(char)
            result.append(char)

            return False

        for char in graphs:
            if dfs(char):
                return ""

        return "".join(result)