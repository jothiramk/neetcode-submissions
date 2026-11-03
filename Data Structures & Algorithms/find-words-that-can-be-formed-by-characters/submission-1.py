class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        # print(char_count)
        res = 0
        for word in words:
            word_count = Counter(word)
            # print(word_count)
            match = True
            for key, value in word_count.items():
                if char_count[key] < value:
                    match = False
                    break
            if match:
                res += len(word)
        
        return res
