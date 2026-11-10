class Solution:
    def compress(self, chars: List[str]) -> int:
        i, k = 0, 0
        n = len(chars)

        while i < n :
            k += 1
            j = i

            while j < n and chars[i] == chars[j]:
                j+=1       
            # j is 5 and i is 3 and k is 3     
            if (j - i) > 1:
                chars[k-1] = chars[i]
                for ch in str(j-i):
                    chars[k] = ch
                    k+=1
                    # k here is 2
                # chars[k]= chars[j]
            else:
                chars[k-1] = chars[i]
            i = j
        # print(f'k is {k}')
        return k

       

            
