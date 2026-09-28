class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = defaultdict(list)
        result = []
        for word in strs:
            grp_anagrams[tuple(sorted(word))].append(word)
        
        # print(dict(grp_anagrams))
        for value in grp_anagrams.values():
            result.append(list(value))
        
        return result
