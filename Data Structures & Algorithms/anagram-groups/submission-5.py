class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        process_map = {}

        for word in strs:
            sorted_word = sorted(word)
            map_key = "".join(sorted_word)
            if map_key not in process_map:
                process_map[map_key] = [word]
            else:
                process_map[map_key].append(word)

            
        
        for value in process_map.values():
            result.append(value)
        
        return result