class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounter = Counter(chars) #o(n)
        result = 0
        for word in words: #(n)
            wordCounter = Counter(word) #(o(n))
            result += len(word)
            for key, val in wordCounter.items():
                if charCounter[key] < val:
                    result -= len(word)
                    break
            
        
        return result
