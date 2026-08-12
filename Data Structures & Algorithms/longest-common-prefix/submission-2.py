class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_min = len(strs[0])
        for i in range(1,len(strs)):
            res = 0 
            word2 = strs[i]
            word1 = strs[i-1]

            j, k = 0, 0
            word1_size = len(word1)
            word2_size = len(word2)

            while j< word1_size and  k < word2_size :
                if word1[j] == word2[k]:
                    res +=1
                else:
                    break
                j+=1
                k+=1
                # print(res)

            prefix_min = min(prefix_min,res)

        return strs[0][0:prefix_min]

            
