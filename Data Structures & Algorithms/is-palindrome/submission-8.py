class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True
        i = 0
        j = n-1
        s = s.lower()
        while i <= j:
            # print(f' i is {i} and {s[i]} and {j} and {s[j]}')
            while not s[i].isalnum():
                i+=1
                if i > j:
                    return True
            while not s[j].isalnum():
                j-=1
                if j < i:
                    return True
            if  s[i]!= s[j]:
                # print(f' before false i is {i} and {s[i]} and {j} and {s[j]}')
                return False
            i+=1
            j-=1
        return True
