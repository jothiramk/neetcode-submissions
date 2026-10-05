class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dict_1 = {'1':'1','0':'0','8':'8','6':'9','9':'6'}
        
        i = 0
        j = len(num)-1


        while i <= j :
            if num[j] not in dict_1:
                return False
            if dict_1[num[j]] != num[i] :
                return False
            i+=1
            j-=1
        return True 

