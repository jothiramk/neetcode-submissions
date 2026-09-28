class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = defaultdict(list)
        result = []
        for word in strs:
            grp_anagrams[tuple(sorted(word))].append(word)
        
        
        return list(grp_anagrams.values())
