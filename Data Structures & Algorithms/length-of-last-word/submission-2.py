class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # last_index = s.rfind(" ")
        # print(last_index)
        # last_word = s[last_index+1:]
        # res = 0
        # for ch in range(last_index+1):
        #     if s[ch].isalpha():
        #         res+=1
        
        # return res
        s_list = s.split()
        print(s_list)
        return len(s_list[-1])

