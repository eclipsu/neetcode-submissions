from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList or beginWord == endWord:
            return 0
        
        neighbours = defaultdict(list)

        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                transform = word[:i] + "*" + word[i + 1:]
                neighbours[transform].append(word)
        
        seen = set(beginWord)
        queue = deque([(beginWord, 1)]) 

        while queue:
            word, distance = queue.popleft()

            seen.add(word)
            if word == endWord:
                return distance
            
            for i in range(length):
                transform = word[:i] + "*" + word[i + 1:]
                possible_words = neighbours[transform]

                for possible_word in possible_words:
                    if possible_word not in seen:
                        queue.append((possible_word, distance + 1))
            
        return 0

        