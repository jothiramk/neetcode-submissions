class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagram_map = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            annagram_map[tuple(sorted_word)].append(word)
        
        return (list(annagram_map.values()))