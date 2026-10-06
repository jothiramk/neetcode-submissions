class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1],[1,1]]
        print(pascal)
        i = 2
        for i in range(2,rowIndex+1):
            sublist = pascal[i-1]
            # print(sublist)
            temp = []
            first_element= sublist[0]
            temp.append(first_element)
            last_element = sublist[len(sublist)-1]
            for i in range(1,len(sublist)):
                temp.append(sublist[i-1]+sublist[i])
            temp.append(last_element)
            pascal.append(temp)
            # print(pascal)
            if i == rowIndex:
                break
        
        return pascal[rowIndex]



