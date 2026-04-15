from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### goal is to create a dict with char count key and str that matches char count valuoe
        ### logic is char1:count,char2:count,char3:count:[word1, word2]
        ### but since we can't have "array of keys-value pair as keys"
        ### we will use array (index being count, element at index  i being letter)
        ### also since we can't have arrays as keys in dict, we will use tuples
        
        collect = defaultdict(list)

        for string in strs:
            space = [0] * 26
            for char in string:
                space[ord(char) - ord("a")] += 1
            collect[tuple(space)].append(string)
        
        return (list(collect.values()))

