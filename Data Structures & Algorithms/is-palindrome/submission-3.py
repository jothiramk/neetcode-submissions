class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        sl = s.lower()
        print(sl)
        while i < j:
            while i < j and not sl[i].isalnum():
                i+=1
            while j > i and not sl[j].isalnum():
                j-=1
            # print(f's[i] is {sl[i]} and {sl[j]}')
            if sl[i] != sl[j]:
                return False
            else:
                i+=1
                j-=1
        return True
