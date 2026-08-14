class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for str in strs:
            space = [0] * 26
            for s in str:
                space[ord(s) - ord("a")] += 1
            anagrams[tuple(space)].append(str)
        
        return(list(anagrams.values()))