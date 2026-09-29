class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounter = Counter(chars)
        result = 0
        for word in words:
            wordCounter = Counter(word)
            result += len(word)
            for key, val in wordCounter.items():
                if charCounter[key] < val:
                    result -= len(word)
                    break
            
        
        return result
