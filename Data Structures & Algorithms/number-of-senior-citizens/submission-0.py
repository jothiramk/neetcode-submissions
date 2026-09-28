class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for person in details:
            age = int(person[11:13])
            print(age)
            if age > 60:
                res+=1
        
        return res



        