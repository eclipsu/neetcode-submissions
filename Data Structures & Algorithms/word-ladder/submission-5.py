from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        
        word_length = len(beginWord)
        neighbours = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(word_length):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbours[pattern].append(word)
        
        seen = set()
        queue = deque([(beginWord, 1)])

        while queue:
            word, distance = queue.popleft()

            if word == endWord:
                return distance

            seen.add(word)

            for i in range(word_length):
                pattern = word[:i] + "*" + word[i + 1:]

                potential_words = neighbours[pattern]
                
                for potential_word in potential_words:
                    if potential_word not in seen:
                        queue.append((potential_word, distance + 1))
                
            
        return 0


