class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        i = k = 0

        while i < size:
            # print(f'i index {i} and k {k}')
            chars[k] = chars[i]
            k+=1
            if k == size:
                return k 
            count = 0
            j = i+1
            while j < size and chars[i]==chars[j]:
                count+=1
                j+=1
            # print(f'cointer is {count} and string is {str(count)}')
            if count > 0:
                for cnt in str(count+1):
                    # print(f'ch is {cnt}')
                    chars[k] = cnt
                    k+=1
                    print(chars)
            i = j
        
        return k

