class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        

        size = len(sentence1)
        size1 = len(sentence2)
        if size != size1:
            return False
        i = 0
        while i < size:
            word1, word2 = sentence1[i], sentence2[i]
            if word1 != word2:
                found = False
                for pair in similarPairs:
                    if (pair[0] == word1 and pair[1] == word2) or (pair[0] == word2 and pair[1] == word1):
                        found = True
                        break
                if not found:
                    return False
            i+=1
        
        return True