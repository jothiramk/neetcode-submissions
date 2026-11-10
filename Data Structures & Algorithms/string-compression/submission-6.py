class Solution:
    def compress(self, chars: List[str]) -> int:
        i, k = 0, 0
        n = len(chars)

        while i < n :
            #write chars[i] at position k and increment k
            chars[k] = chars[i]
            k += 1
            j = i

            while j < n and chars[i] == chars[j]:
                j+=1       
            if (j - i) > 1:                
                for ch in str(j-i):
                    chars[k] = ch
                    k+=1
            i = j
        return k

       

            
