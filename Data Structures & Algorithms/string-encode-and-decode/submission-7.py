class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            n = len(word)
            res += str(n)+'#'+word
        # print (res)
        return res


    def decode(self, s: str) -> List[str]:
        print(s)
        size = len(s)
        i = 0
        start = 0
        res = []
        while i < size:
            delim_index = s.find('#',i)       
            str_len = s[start:delim_index]
            # print(f'delim_index is {delim_index} and {str_len}')
            word_len = int(str_len)
            word_to_append = s[delim_index+1 : delim_index+1+word_len]
            # print(f'word_to_append {word_to_append}')
            res.append(word_to_append)
            i=delim_index+word_len+1
            start=i
            # print(f'fiinal result {res} and {i} and {start}')

        
        return res
            