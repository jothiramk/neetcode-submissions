class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        
        for key, value in ransomCounter.items():
            
            if magazineCounter[key] < value:
                return False        

        return True