class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        size1 = len(sentence1)
        size2 = len(sentence2)
        
        if size1 != size2:
            return False
        
        pair_dict = defaultdict(set)
        for pair in similarPairs:
            pair_dict[pair[0]].add(pair[1])
            pair_dict[pair[1]].add(pair[0])
        
        i = 0
        
        while i < size1:
            found = False
            word1 = sentence1[i]
            word2 = sentence2[i]

            if word1 == word2:
                found = True

            if word2 in pair_dict[word1] or word1 in pair_dict[word2]:
                found = True
            elif not found:
                return False
            
            i+=1
            # print(f'i is {i} and {word1} and {word2}')


        return True
