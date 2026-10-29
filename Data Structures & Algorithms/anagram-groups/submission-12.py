class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            anagram_map["".join(sorted_word)].append(word)
        
        return list(anagram_map.values())
            