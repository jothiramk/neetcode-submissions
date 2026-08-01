class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        process_map = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            map_key = "".join(sorted_word)
            process_map[map_key].append(word)

     
        for value in process_map.values():
            result.append(value)
        
        return result