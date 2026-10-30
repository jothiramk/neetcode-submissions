class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        print(s1_sorted)
        n = len(s1)
        print(f'value of n is {n}')
        l = 0
        s2_substr = []
        for r in range(len(s2)):
            s2_substr.append(s2[r])
            # print(f'appengin {s2_substr}')
            if r-l+1 == n:
                sorted_s2 = sorted(s2_substr)
                if sorted_s2==s1_sorted:
                    return True
                else:
                    #reduce the window
                    l = l +1
                    # print(f'before popping {s2_substr}')
                    s2_substr.pop(0)
                    # print(f'after popping {s2_substr}')          
        return False
               
            
            
            
            
        
        return False

            